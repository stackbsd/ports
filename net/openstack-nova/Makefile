PORTNAME=	nova
DISTVERSION=	33.0.2
CATEGORIES=	net python
PKGNAMEPREFIX=	openstack-

MAINTAINER=	josh@joshh.info
COMMENT=	OpenStack Compute service (Nova)
WWW=		https://docs.openstack.org/nova/

LICENSE=	APACHE20

BUILD_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime

LIB_DEPENDS=	libopenblas.so:math/openblas

RUN_DEPENDS=	novnc>0:www/novnc \
		openstack-runtime>=2026.1.0:net/openstack-runtime \
		sudo:security/sudo \
		xorrisofs:sysutils/xorriso

USE_RC_SUBR=	nova-api nova-scheduler nova-conductor nova-compute \
		nova-novncproxy

SUB_FILES=	nova-api.sh nova-compute.sh nova-conductor.sh nova-manage.sh \
		nova-novncproxy.sh nova-rootwrap.sh nova-scheduler.sh \
		nova-status.sh nova.conf rootwrap.conf sudoers
SUB_LIST=	VENV=${VENV}

USERS=		nova
GROUPS=		nova

PLIST_SUB=	VENV=libexec/openstack

# the distfile set and the wheel engine shared with the other openstack ports
.include "${.CURDIR}/../openstack-runtime/Makefile.venv"

do-install:
	${SETENV} PYTHONPATH=${PYTHON_SITELIBDIR} \
		${LOCALBASE}/libexec/openstack/bin/python${PYTHON_VER} -m installer \
		--destdir ${STAGEDIR} --prefix ${VENV} --no-compile-bytecode \
		${WHEELDIR}/*.whl

post-install:
	${INSTALL_SCRIPT} ${WRKDIR}/nova-api.sh ${STAGEDIR}${PREFIX}/bin/nova-api
	${INSTALL_SCRIPT} ${WRKDIR}/nova-compute.sh ${STAGEDIR}${PREFIX}/bin/nova-compute
	${INSTALL_SCRIPT} ${WRKDIR}/nova-conductor.sh ${STAGEDIR}${PREFIX}/bin/nova-conductor
	${INSTALL_SCRIPT} ${WRKDIR}/nova-manage.sh ${STAGEDIR}${PREFIX}/bin/nova-manage
	${INSTALL_SCRIPT} ${WRKDIR}/nova-novncproxy.sh ${STAGEDIR}${PREFIX}/bin/nova-novncproxy
	${INSTALL_SCRIPT} ${WRKDIR}/nova-rootwrap.sh ${STAGEDIR}${PREFIX}/bin/nova-rootwrap
	${INSTALL_SCRIPT} ${WRKDIR}/nova-scheduler.sh ${STAGEDIR}${PREFIX}/bin/nova-scheduler
	${INSTALL_SCRIPT} ${WRKDIR}/nova-status.sh ${STAGEDIR}${PREFIX}/bin/nova-status
	@${MKDIR} ${STAGEDIR}${ETCDIR} ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d \
		${STAGEDIR}${PREFIX}/etc/sudoers.d
	${INSTALL_DATA} ${WRKDIR}/nova.conf ${STAGEDIR}${ETCDIR}/nova.conf.sample
	${INSTALL_DATA} ${FILESDIR}/nova-wsgi.conf ${STAGEDIR}${ETCDIR}/nova-wsgi.conf.sample
	${INSTALL_DATA} ${WRKDIR}/rootwrap.conf ${STAGEDIR}${ETCDIR}/rootwrap.conf.sample
	${INSTALL_DATA} ${STAGEDIR}${VENV}/etc/nova/api-paste.ini ${STAGEDIR}${ETCDIR}
	${INSTALL_DATA} ${WRKDIR}/sudoers ${STAGEDIR}${PREFIX}/etc/sudoers.d/openstack-nova
	${INSTALL_DATA} ${FILESDIR}/nova-log.conf ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d

.include <bsd.port.mk>
