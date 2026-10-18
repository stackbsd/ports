PORTNAME=	neutron-bsdbridge
DISTVERSION=	0.9.3
CATEGORIES=	net python
MASTER_SITES=	PYPI
DISTNAME=	${PORTNAME:S/-/_/g}-${DISTVERSION}

MAINTAINER=	josh@joshh.info
COMMENT=	if_bridge and pf based ML2 driver and agents for OpenStack Neutron
WWW=		https://github.com/stackbsd/neutron-bsdbridge

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}uv-build>=0.11.28:devel/py-uv-build@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>0:devel/py-wheel@${PY_FLAVOR} \
		openstack-runtime>=2026.1.0:net/openstack-runtime

RUN_DEPENDS=	dnsmasq:dns/dnsmasq \
		openstack-neutron>=28.0.1:net/openstack-neutron \
		openstack-runtime>=2026.1.0:net/openstack-runtime

USES=		python:3.12 shebangfix
USE_PYTHON=	noflavors pep517
USE_RC_SUBR=	neutron-bsdbridge-l2-agent neutron-bsdbridge-dhcp-agent \
		neutron-bsdbridge-l3-agent
SHEBANG_GLOB=	*.py
python_CMD=	${VENV}/bin/python${PYTHON_VER}

NO_ARCH=	yes
SUB_FILES=	bsdbridge_agent.ini neutron-bsdbridge-dhcp-agent.sh \
		neutron-bsdbridge-l2-agent.sh neutron-bsdbridge-l3-agent.sh
SUB_LIST=	VENV=${VENV}

ETCDIR=		${PREFIX}/etc/neutron
PLIST_SUB=	VENV=libexec/openstack

# the shared venv from net/openstack-runtime
VENV=		${PREFIX}/libexec/openstack

do-install:
	${SETENV} PYTHONPATH=${PYTHON_SITELIBDIR} \
		${LOCALBASE}/libexec/openstack/bin/python${PYTHON_VER} -m installer \
		--destdir ${STAGEDIR} --prefix ${VENV} --no-compile-bytecode \
		${WRKSRC}/dist/*.whl

post-install:
	${INSTALL_SCRIPT} ${WRKDIR}/neutron-bsdbridge-dhcp-agent.sh ${STAGEDIR}${PREFIX}/bin/neutron-bsdbridge-dhcp-agent
	${INSTALL_SCRIPT} ${WRKDIR}/neutron-bsdbridge-l2-agent.sh ${STAGEDIR}${PREFIX}/bin/neutron-bsdbridge-l2-agent
	${INSTALL_SCRIPT} ${WRKDIR}/neutron-bsdbridge-l3-agent.sh ${STAGEDIR}${PREFIX}/bin/neutron-bsdbridge-l3-agent
	@${MKDIR} ${STAGEDIR}${ETCDIR} ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d
	${INSTALL_DATA} ${WRKDIR}/bsdbridge_agent.ini ${STAGEDIR}${ETCDIR}/bsdbridge_agent.ini.sample
	${INSTALL_DATA} ${FILESDIR}/neutron-bsdbridge-log.conf ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d
	${PYTHON_CMD} -m compileall -q -j0 -s ${STAGEDIR} -p / ${STAGEDIR}${VENV}/lib

.include <bsd.port.mk>
