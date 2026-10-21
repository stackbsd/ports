PORTNAME=	designate
DISTVERSION=	22.0.0
CATEGORIES=	net python
PKGNAMEPREFIX=	openstack-

MAINTAINER=	josh@joshh.info
COMMENT=	OpenStack DNS service (Designate)
WWW=		https://docs.openstack.org/designate/

LICENSE=	APACHE20

BUILD_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime

RUN_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime \
		sudo:security/sudo

USE_RC_SUBR=	designate-api designate-central designate-mdns \
		designate-producer designate-worker

NO_ARCH=	yes
SUB_FILES=	designate-api.sh designate-central.sh designate-manage.sh \
		designate-mdns.sh designate-producer.sh designate-rootwrap.sh \
		designate-status.sh designate-worker.sh designate.conf \
		pools.yaml rootwrap.conf sudoers
SUB_LIST=	VENV=${VENV}

USERS=		designate
GROUPS=		designate

PLIST_SUB=	VENV=libexec/openstack

# the distfile set and the wheel engine shared with the other openstack ports
.include "${.CURDIR}/../openstack-runtime/Makefile.venv"

do-install:
	${SETENV} PYTHONPATH=${PYTHON_SITELIBDIR} \
		${LOCALBASE}/libexec/openstack/bin/python${PYTHON_VER} -m installer \
		--destdir ${STAGEDIR} --prefix ${VENV} --no-compile-bytecode \
		${WHEELDIR}/*.whl

post-install:
	${INSTALL_SCRIPT} ${WRKDIR}/designate-api.sh ${STAGEDIR}${PREFIX}/bin/designate-api
	${INSTALL_SCRIPT} ${WRKDIR}/designate-central.sh ${STAGEDIR}${PREFIX}/bin/designate-central
	${INSTALL_SCRIPT} ${WRKDIR}/designate-manage.sh ${STAGEDIR}${PREFIX}/bin/designate-manage
	${INSTALL_SCRIPT} ${WRKDIR}/designate-mdns.sh ${STAGEDIR}${PREFIX}/bin/designate-mdns
	${INSTALL_SCRIPT} ${WRKDIR}/designate-producer.sh ${STAGEDIR}${PREFIX}/bin/designate-producer
	${INSTALL_SCRIPT} ${WRKDIR}/designate-rootwrap.sh ${STAGEDIR}${PREFIX}/bin/designate-rootwrap
	${INSTALL_SCRIPT} ${WRKDIR}/designate-status.sh ${STAGEDIR}${PREFIX}/bin/designate-status
	${INSTALL_SCRIPT} ${WRKDIR}/designate-worker.sh ${STAGEDIR}${PREFIX}/bin/designate-worker
	@${MKDIR} ${STAGEDIR}${ETCDIR}/rootwrap.d ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d \
		${STAGEDIR}${PREFIX}/etc/sudoers.d
	${INSTALL_DATA} ${WRKDIR}/designate.conf ${STAGEDIR}${ETCDIR}/designate.conf.sample
	${INSTALL_DATA} ${FILESDIR}/designate-wsgi.conf ${STAGEDIR}${ETCDIR}/designate-wsgi.conf.sample
	${INSTALL_DATA} ${WRKDIR}/pools.yaml ${STAGEDIR}${ETCDIR}/pools.yaml.sample
	${INSTALL_DATA} ${WRKDIR}/rootwrap.conf ${STAGEDIR}${ETCDIR}/rootwrap.conf.sample
	${INSTALL_DATA} ${FILESDIR}/bind9.filters ${STAGEDIR}${ETCDIR}/rootwrap.d
	${INSTALL_DATA} ${STAGEDIR}${VENV}/etc/designate/api-paste.ini ${STAGEDIR}${ETCDIR}
	${INSTALL_DATA} ${WRKDIR}/sudoers ${STAGEDIR}${PREFIX}/etc/sudoers.d/openstack-designate
	${INSTALL_DATA} ${FILESDIR}/designate-log.conf ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d

.include <bsd.port.mk>
