PORTNAME=	placement
DISTVERSION=	15.0.0
CATEGORIES=	net python
PKGNAMEPREFIX=	openstack-

MAINTAINER=	5124298+joshiggins@users.noreply.github.com
COMMENT=	OpenStack Placement service
WWW=		https://docs.openstack.org/placement/

LICENSE=	APACHE20

BUILD_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime

RUN_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime

USE_RC_SUBR=	placement-api

NO_ARCH=	yes
SUB_FILES=	placement-api.sh placement-manage.sh placement-status.sh
SUB_LIST=	VENV=${VENV}

USERS=		placement
GROUPS=		placement

PLIST_SUB=	VENV=libexec/openstack

# the distfile set and the wheel engine shared with the other openstack ports
.include "${.CURDIR}/../openstack-runtime/Makefile.venv"

do-install:
	${SETENV} PYTHONPATH=${PYTHON_SITELIBDIR} \
		${LOCALBASE}/libexec/openstack/bin/python${PYTHON_VER} -m installer \
		--destdir ${STAGEDIR} --prefix ${VENV} --no-compile-bytecode \
		${WHEELDIR}/*.whl

post-install:
	${INSTALL_SCRIPT} ${WRKDIR}/placement-api.sh ${STAGEDIR}${PREFIX}/bin/placement-api
	${INSTALL_SCRIPT} ${WRKDIR}/placement-manage.sh ${STAGEDIR}${PREFIX}/bin/placement-manage
	${INSTALL_SCRIPT} ${WRKDIR}/placement-status.sh ${STAGEDIR}${PREFIX}/bin/placement-status
	@${MKDIR} ${STAGEDIR}${ETCDIR} ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d
	${INSTALL_DATA} ${FILESDIR}/placement.conf ${STAGEDIR}${ETCDIR}/placement.conf.sample
	${INSTALL_DATA} ${FILESDIR}/placement-wsgi.conf ${STAGEDIR}${ETCDIR}/placement-wsgi.conf.sample
	${INSTALL_DATA} ${FILESDIR}/placement-log.conf ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d

.include <bsd.port.mk>
