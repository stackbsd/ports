# Linux capabilities do not exist on FreeBSD

--- oslo_privsep-3.10.1/oslo_privsep/capabilities.py.orig	2026-02-23 16:27:02.000000000 +0000
+++ oslo_privsep-3.10.1/oslo_privsep/capabilities.py	2026-09-04 12:30:11.417567000 +0100
@@ -177,11 +177,17 @@
     _capget = crt.capget
     _capset = crt.capset
 else:
+    crt = None
     _prctl = None
     _capget = None
     _capset = None
 
 
+def is_supported() -> bool:
+    """Report whether this platform supports capabilities"""
+    return _capset is not None
+
+
 def set_keepcaps(enable: bool) -> None:
     """Set/unset thread's "keep capabilities" flag - see prctl(2)"""
     ret = _prctl(crt.PR_SET_KEEPCAPS, ffi.cast('unsigned long', bool(enable)))
