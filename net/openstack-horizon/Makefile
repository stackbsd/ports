PORTNAME=	horizon
DISTVERSION=	25.7.3
CATEGORIES=	net python
PKGNAMEPREFIX=	openstack-

MAINTAINER=	josh@joshh.info
COMMENT=	OpenStack Dashboard (Horizon)
WWW=		https://docs.openstack.org/horizon/

LICENSE=	APACHE20

BUILD_DEPENDS=	msgfmt:devel/gettext-tools \
		openstack-runtime>=2026.1.0:net/openstack-runtime

LIB_DEPENDS=	libjpeg.so:graphics/jpeg-turbo

RUN_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime

USE_RC_SUBR=	horizon

SUB_FILES=	build_settings.py horizon.sh horizon-manage.sh local_settings.py \
		pkg-message
SUB_LIST=	VENV=${VENV} STATIC_ROOT=${STAGEDIR}${STATICDIR}

USERS=		horizon
GROUPS=		horizon

PLIST_SUB=	VENV=libexec/openstack

SITEPKGS=	${VENV}/lib/python${PYTHON_VER}/site-packages
DASHBOARD=	${SITEPKGS}/openstack_dashboard
STATICDIR=	${PREFIX}/www/horizon/static

# django-admin against the staged package under the runtime interpreter
DJANGO=		${SETENV} PYTHONPATH=${STAGEDIR}${SITEPKGS} \
		DJANGO_SETTINGS_MODULE=openstack_dashboard.settings \
		${LOCALBASE}/libexec/openstack/bin/python${PYTHON_VER} -m django

# the distfile set and the wheel engine shared with the other openstack ports
.include "${.CURDIR}/../openstack-runtime/Makefile.venv"

do-install:
	${SETENV} PYTHONPATH=${PYTHON_SITELIBDIR} \
		${LOCALBASE}/libexec/openstack/bin/python${PYTHON_VER} -m installer \
		--destdir ${STAGEDIR} --prefix ${VENV} --no-compile-bytecode \
		${WHEELDIR}/*.whl

post-install:
	${INSTALL_SCRIPT} ${WRKDIR}/horizon.sh ${STAGEDIR}${PREFIX}/bin/horizon
	${INSTALL_SCRIPT} ${WRKDIR}/horizon-manage.sh ${STAGEDIR}${PREFIX}/bin/horizon-manage
	@${MKDIR} ${STAGEDIR}${ETCDIR} ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d
	${INSTALL_DATA} ${WRKDIR}/local_settings.py ${STAGEDIR}${ETCDIR}/local_settings.py.sample
	${INSTALL_DATA} ${FILESDIR}/horizon-wsgi.conf ${STAGEDIR}${ETCDIR}/horizon-wsgi.conf.sample
	${INSTALL_DATA} ${FILESDIR}/horizon-log.conf ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d
# compile the translations and collect and compress the static tree under the build settings
	${INSTALL_DATA} ${WRKDIR}/build_settings.py ${STAGEDIR}${DASHBOARD}/local/local_settings.py
.for pkg in horizon openstack_auth openstack_dashboard
	cd ${STAGEDIR}${SITEPKGS}/${pkg} && ${DJANGO} compilemessages
.endfor
	${DJANGO} collectstatic --noinput
	${DJANGO} compress --force
	${RM} -r ${STAGEDIR}${DASHBOARD}/local/local_settings.py \
		${STAGEDIR}${DASHBOARD}/local/__pycache__
	@cd ${STAGEDIR}${PREFIX} && ${FIND} www/horizon -type f | ${SORT} >> ${TMPPLIST}
# the operator's settings live in ETCDIR and horizon imports local.local_settings
	${LN} -sf ${ETCDIR}/local_settings.py ${STAGEDIR}${DASHBOARD}/local/local_settings.py

.include <bsd.port.mk>
