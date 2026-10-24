PORTNAME=	cinder-zfs-driver
DISTVERSION=	0.9.1
CATEGORIES=	net python
MASTER_SITES=	PYPI
DISTNAME=	${PORTNAME:S/-/_/g}-${DISTVERSION}

MAINTAINER=	josh@joshh.info
COMMENT=	ZFS volume driver for OpenStack Cinder
WWW=		https://github.com/stackbsd/cinder-zfs-driver

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}uv-build>=0.11.28:devel/py-uv-build@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>0:devel/py-wheel@${PY_FLAVOR} \
		openstack-runtime>=2026.1.0:net/openstack-runtime
RUN_DEPENDS=	openstack-cinder>=28.0.0:net/openstack-cinder \
		openstack-runtime>=2026.1.0:net/openstack-runtime

USES=		python:3.12 shebangfix
USE_PYTHON=	noflavors pep517
SHEBANG_GLOB=	*.py
python_CMD=	${VENV}/bin/python${PYTHON_VER}

NO_ARCH=	yes

SUB_FILES=	pkg-message

PLIST_SUB=	VENV=libexec/openstack

# the shared venv from net/openstack-runtime
VENV=		${PREFIX}/libexec/openstack

do-install:
	${SETENV} PYTHONPATH=${PYTHON_SITELIBDIR} \
		${LOCALBASE}/libexec/openstack/bin/python${PYTHON_VER} -m installer \
		--destdir ${STAGEDIR} --prefix ${VENV} --no-compile-bytecode \
		${WRKSRC}/dist/*.whl

post-install:
	${PYTHON_CMD} -m compileall -q -j0 -s ${STAGEDIR} -p / ${STAGEDIR}${VENV}/lib

.include <bsd.port.mk>
