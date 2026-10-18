# Linux capabilities do not exist on FreeBSD

--- oslo_privsep-3.10.1/oslo_privsep/daemon.py.orig	2026-02-23 16:27:02.000000000 +0000
+++ oslo_privsep-3.10.1/oslo_privsep/daemon.py	2026-09-04 12:30:11.443463000 +0100
@@ -77,7 +77,7 @@
 if TYPE_CHECKING:
     from oslo_privsep import priv_context
 
-if platform.system() == 'Linux':
+if platform.system() != 'Windows':
     import fcntl
     import grp
     import pwd
@@ -466,7 +466,8 @@
     def _drop_privs(self) -> None:
         try:
             # Keep current capabilities across setuid away from root.
-            capabilities.set_keepcaps(True)
+            if capabilities.is_supported():
+                capabilities.set_keepcaps(True)
 
             if self.group is not None:
                 try:
@@ -481,13 +482,22 @@
                 setuid(self.user)
 
         finally:
-            capabilities.set_keepcaps(False)
+            if capabilities.is_supported():
+                capabilities.set_keepcaps(False)
 
         LOG.info(
             'privsep process running with uid/gid: %(uid)s/%(gid)s',
             {'uid': os.getuid(), 'gid': os.getgid()},
         )
 
+        if not capabilities.is_supported():
+            LOG.warning(
+                'capabilities are not supported on %(platform)s, so the '
+                'privsep daemon retains the privileges it started with',
+                {'platform': platform.system()},
+            )
+            return
+
         capabilities.drop_all_caps_except(self.caps, self.caps, [])
 
         def fmt_caps(capset: Iterable[int]) -> str:
