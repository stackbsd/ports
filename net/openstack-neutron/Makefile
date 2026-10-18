PORTNAME=	neutron
DISTVERSION=	28.0.1
CATEGORIES=	net python
PKGNAMEPREFIX=	openstack-

MAINTAINER=	josh@joshh.info
COMMENT=	OpenStack Networking service (Neutron)
WWW=		https://docs.openstack.org/neutron/

LICENSE=	APACHE20

BUILD_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime

RUN_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime

USE_RC_SUBR=	neutron-api neutron-rpc-server

NO_ARCH=	yes

SUB_FILES=	neutron-api.sh neutron-db-manage.sh neutron-rpc-server.sh \
		neutron-status.sh neutron.conf
SUB_LIST=	VENV=${VENV}

USERS=		neutron
GROUPS=		neutron

PLIST_SUB=	VENV=libexec/openstack

# the distfile set and the wheel engine shared with the other openstack ports
.include "${.CURDIR}/../openstack-runtime/Makefile.venv"

do-install:
	${SETENV} PYTHONPATH=${PYTHON_SITELIBDIR} \
		${LOCALBASE}/libexec/openstack/bin/python${PYTHON_VER} -m installer \
		--destdir ${STAGEDIR} --prefix ${VENV} --no-compile-bytecode \
		${WHEELDIR}/*.whl

post-install:
	${INSTALL_SCRIPT} ${WRKDIR}/neutron-api.sh ${STAGEDIR}${PREFIX}/bin/neutron-api
	${INSTALL_SCRIPT} ${WRKDIR}/neutron-db-manage.sh ${STAGEDIR}${PREFIX}/bin/neutron-db-manage
	${INSTALL_SCRIPT} ${WRKDIR}/neutron-rpc-server.sh ${STAGEDIR}${PREFIX}/bin/neutron-rpc-server
	${INSTALL_SCRIPT} ${WRKDIR}/neutron-status.sh ${STAGEDIR}${PREFIX}/bin/neutron-status
	@${MKDIR} ${STAGEDIR}${ETCDIR}/plugins/ml2 ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d
	${INSTALL_DATA} ${WRKDIR}/neutron.conf ${STAGEDIR}${ETCDIR}/neutron.conf.sample
	${INSTALL_DATA} ${FILESDIR}/neutron-wsgi.conf ${STAGEDIR}${ETCDIR}/neutron-wsgi.conf.sample
	${INSTALL_DATA} ${FILESDIR}/ml2_conf.ini ${STAGEDIR}${ETCDIR}/plugins/ml2/ml2_conf.ini.sample
	${INSTALL_DATA} ${STAGEDIR}${VENV}/etc/neutron/api-paste.ini ${STAGEDIR}${ETCDIR}
	${INSTALL_DATA} ${FILESDIR}/neutron-log.conf ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d

.include <bsd.port.mk>
