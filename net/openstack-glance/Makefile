PORTNAME=	glance
DISTVERSION=	32.0.0
CATEGORIES=	net python
PKGNAMEPREFIX=	openstack-

MAINTAINER=	5124298+joshiggins@users.noreply.github.com
COMMENT=	OpenStack Image service (Glance)
WWW=		https://docs.openstack.org/glance/

LICENSE=	APACHE20

BUILD_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime

RUN_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime \
		qemu-img:emulators/qemu@tools

USE_RC_SUBR=	glance-api

NO_ARCH=	yes
SUB_FILES=	glance-api.sh glance-manage.sh glance-status.sh
SUB_LIST=	VENV=${VENV}

USERS=		glance
GROUPS=		glance

PLIST_SUB=	VENV=libexec/openstack

# the distfile set and the wheel engine shared with the other openstack ports
.include "${.CURDIR}/../openstack-runtime/Makefile.venv"

do-install:
	${SETENV} PYTHONPATH=${PYTHON_SITELIBDIR} \
		${LOCALBASE}/libexec/openstack/bin/python${PYTHON_VER} -m installer \
		--destdir ${STAGEDIR} --prefix ${VENV} --no-compile-bytecode \
		${WHEELDIR}/*.whl

post-install:
	${INSTALL_SCRIPT} ${WRKDIR}/glance-api.sh ${STAGEDIR}${PREFIX}/bin/glance-api
	${INSTALL_SCRIPT} ${WRKDIR}/glance-manage.sh ${STAGEDIR}${PREFIX}/bin/glance-manage
	${INSTALL_SCRIPT} ${WRKDIR}/glance-status.sh ${STAGEDIR}${PREFIX}/bin/glance-status
	@${MKDIR} ${STAGEDIR}${ETCDIR} ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d
	${INSTALL_DATA} ${FILESDIR}/glance-api.conf ${STAGEDIR}${ETCDIR}/glance-api.conf.sample
	${INSTALL_DATA} ${FILESDIR}/glance-wsgi.conf ${STAGEDIR}${ETCDIR}/glance-wsgi.conf.sample
	${INSTALL_DATA} ${STAGEDIR}${VENV}/etc/glance/glance-api-paste.ini ${STAGEDIR}${ETCDIR}
	${INSTALL_DATA} ${FILESDIR}/glance-log.conf ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d

.include <bsd.port.mk>
