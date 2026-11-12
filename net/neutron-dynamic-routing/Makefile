PORTNAME=	neutron-dynamic-routing
DISTVERSION=	28.0.0
CATEGORIES=	net python

MAINTAINER=	josh@joshh.info
COMMENT=	BGP dynamic routing service for OpenStack Neutron
WWW=		https://docs.openstack.org/neutron-dynamic-routing/

LICENSE=	APACHE20

BUILD_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime

RUN_DEPENDS=	openstack-neutron>=28.0.1:net/openstack-neutron \
		openstack-runtime>=2026.1.0:net/openstack-runtime

USE_RC_SUBR=	neutron-bgp-dragent

NO_ARCH=	yes

SUB_FILES=	neutron-bgp-dragent.sh pkg-message
SUB_LIST=	VENV=${VENV}

ETCDIR=		${PREFIX}/etc/neutron
PLIST_SUB=	VENV=libexec/openstack

# the distfile set and the wheel engine shared with the other openstack ports
.include "${.CURDIR}/../openstack-runtime/Makefile.venv"

do-install:
	${SETENV} PYTHONPATH=${PYTHON_SITELIBDIR} \
		${LOCALBASE}/libexec/openstack/bin/python${PYTHON_VER} -m installer \
		--destdir ${STAGEDIR} --prefix ${VENV} --no-compile-bytecode \
		${WHEELDIR}/*.whl

post-install:
	${INSTALL_SCRIPT} ${WRKDIR}/neutron-bgp-dragent.sh ${STAGEDIR}${PREFIX}/bin/neutron-bgp-dragent
	@${MKDIR} ${STAGEDIR}${ETCDIR} ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d
	${INSTALL_DATA} ${FILESDIR}/bgp_dragent.ini ${STAGEDIR}${ETCDIR}/bgp_dragent.ini.sample
	${INSTALL_DATA} ${FILESDIR}/neutron-dynamic-routing-log.conf ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d

.include <bsd.port.mk>
