# TCP_USER_TIMEOUT is a Linux-only socket option

--- oslo_messaging-17.3.0/oslo_messaging/_drivers/impl_rabbit.py.orig	2026-02-18 13:45:04.000000000 +0000
+++ oslo_messaging-17.3.0/oslo_messaging/_drivers/impl_rabbit.py	2026-09-04 12:30:11.486758000 +0100
@@ -1271,8 +1271,8 @@
                       self.connection_id, e)
         else:
             sock.settimeout(timeout)
-            # TCP_USER_TIMEOUT is not defined on Windows and Mac OS X
-            if sys.platform != 'win32' and sys.platform != 'darwin':
+            # TCP_USER_TIMEOUT is a Linux-only socket option.
+            if sys.platform.startswith('linux'):
                 try:
                     timeout = timeout * 1000 if timeout is not None else 0
                     # NOTE(gdavoian): only integers and strings are allowed
@@ -1284,9 +1284,8 @@
                                     TCP_USER_TIMEOUT,
                                     int(math.ceil(timeout)))
                 except OSError as error:
-                    code = error[0]
                     # TCP_USER_TIMEOUT not defined on kernels <2.6.37
-                    if code != errno.ENOPROTOOPT:
+                    if error.errno != errno.ENOPROTOOPT:
                         raise
 
     @contextlib.contextmanager
