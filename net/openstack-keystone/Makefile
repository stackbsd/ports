PORTNAME=	keystone
DISTVERSION=	29.0.2
CATEGORIES=	net python
PKGNAMEPREFIX=	openstack-

MAINTAINER=	josh@joshh.info
COMMENT=	OpenStack Identity service (Keystone)
WWW=		https://docs.openstack.org/keystone/

LICENSE=	APACHE20

BUILD_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime

RUN_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime

USE_RC_SUBR=	keystone-api

NO_ARCH=	yes
SUB_FILES=	keystone-api.sh keystone-manage.sh keystone-status.sh \
		keystone.conf
SUB_LIST=	VENV=${VENV}

USERS=		keystone
GROUPS=		keystone

PLIST_SUB=	VENV=libexec/openstack

# the distfile set and the wheel engine shared with the other openstack ports
.include "${.CURDIR}/../openstack-runtime/Makefile.venv"

do-install:
	${SETENV} PYTHONPATH=${PYTHON_SITELIBDIR} \
		${LOCALBASE}/libexec/openstack/bin/python${PYTHON_VER} -m installer \
		--destdir ${STAGEDIR} --prefix ${VENV} --no-compile-bytecode \
		${WHEELDIR}/*.whl

post-install:
	${INSTALL_SCRIPT} ${WRKDIR}/keystone-api.sh ${STAGEDIR}${PREFIX}/bin/keystone-api
	${INSTALL_SCRIPT} ${WRKDIR}/keystone-manage.sh ${STAGEDIR}${PREFIX}/bin/keystone-manage
	${INSTALL_SCRIPT} ${WRKDIR}/keystone-status.sh ${STAGEDIR}${PREFIX}/bin/keystone-status
	@${MKDIR} ${STAGEDIR}${ETCDIR} ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d
	${INSTALL_DATA} ${WRKDIR}/keystone.conf ${STAGEDIR}${ETCDIR}/keystone.conf.sample
	${INSTALL_DATA} ${FILESDIR}/keystone-wsgi.conf ${STAGEDIR}${ETCDIR}/keystone-wsgi.conf.sample
	${INSTALL_DATA} ${FILESDIR}/keystone-log.conf ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d

.include <bsd.port.mk>
