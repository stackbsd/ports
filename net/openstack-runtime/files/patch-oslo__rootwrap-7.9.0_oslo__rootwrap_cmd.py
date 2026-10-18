# Use portable os.closerange() to drop fds

--- oslo_rootwrap-7.9.0/oslo_rootwrap/cmd.py.orig	2026-02-20 16:04:57.000000000 +0000
+++ oslo_rootwrap-7.9.0/oslo_rootwrap/cmd.py	2026-09-04 12:30:11.466239000 +0100
@@ -114,13 +114,7 @@
         if fd_limits[0] > sensible_fd_limit:
             # Close any fd beyond sensible_fd_limit prior adjusting our
             # rlimit to ensure all fds are closed
-            for fd_entry in os.listdir('/proc/self/fd'):
-                # NOTE(dmllr): In a previous patch revision non-numeric
-                # dir entries were silently ignored which reviewers
-                # didn't like. Readd exception handling when it occurs.
-                fd = int(fd_entry)
-                if fd >= sensible_fd_limit:
-                    os.close(fd)
+            os.closerange(sensible_fd_limit, fd_limits[0])
             # Unfortunately this inherits to our children, so allow them to
             # re-raise by passing through the hard limit unmodified
             resource.setrlimit(
