PORTNAME=	ironic
DISTVERSION=	35.1.0
CATEGORIES=	net python
PKGNAMEPREFIX=	openstack-

MAINTAINER=	josh@joshh.info
COMMENT=	OpenStack Bare Metal service (Ironic)
WWW=		https://docs.openstack.org/ironic/

LICENSE=	APACHE20

BUILD_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime

RUN_DEPENDS=	ipmitool:sysutils/ipmitool \
		openstack-runtime>=2026.1.0:net/openstack-runtime \
		qemu-img:emulators/qemu@tools

USE_RC_SUBR=	ironic-api ironic-conductor

NO_ARCH=	yes
SUB_FILES=	ironic-api.sh ironic-conductor.sh ironic-dbsync.sh \
		ironic-novncproxy.sh ironic-pxe-filter.sh ironic-status.sh \
		ironic.conf pkg-message
SUB_LIST=	VENV=${VENV}

USERS=		ironic
GROUPS=		ironic

PLIST_SUB=	VENV=libexec/openstack

# the distfile set and the wheel engine shared with the other openstack ports
.include "${.CURDIR}/../openstack-runtime/Makefile.venv"

do-install:
	${SETENV} PYTHONPATH=${PYTHON_SITELIBDIR} \
		${LOCALBASE}/libexec/openstack/bin/python${PYTHON_VER} -m installer \
		--destdir ${STAGEDIR} --prefix ${VENV} --no-compile-bytecode \
		${WHEELDIR}/*.whl

post-install:
	${INSTALL_SCRIPT} ${WRKDIR}/ironic-api.sh ${STAGEDIR}${PREFIX}/bin/ironic-api
	${INSTALL_SCRIPT} ${WRKDIR}/ironic-conductor.sh ${STAGEDIR}${PREFIX}/bin/ironic-conductor
	${INSTALL_SCRIPT} ${WRKDIR}/ironic-dbsync.sh ${STAGEDIR}${PREFIX}/bin/ironic-dbsync
	${INSTALL_SCRIPT} ${WRKDIR}/ironic-novncproxy.sh ${STAGEDIR}${PREFIX}/bin/ironic-novncproxy
	${INSTALL_SCRIPT} ${WRKDIR}/ironic-pxe-filter.sh ${STAGEDIR}${PREFIX}/bin/ironic-pxe-filter
	${INSTALL_SCRIPT} ${WRKDIR}/ironic-status.sh ${STAGEDIR}${PREFIX}/bin/ironic-status
	@${MKDIR} ${STAGEDIR}${ETCDIR} ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d
	${INSTALL_DATA} ${WRKDIR}/ironic.conf ${STAGEDIR}${ETCDIR}/ironic.conf.sample
	${INSTALL_DATA} ${FILESDIR}/ironic-wsgi.conf ${STAGEDIR}${ETCDIR}/ironic-wsgi.conf.sample
	${INSTALL_DATA} ${FILESDIR}/ironic-log.conf ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d

.include <bsd.port.mk>
