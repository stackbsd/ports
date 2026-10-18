PORTNAME=	nova-bhyve
DISTVERSION=	0.9.3
CATEGORIES=	net python
MASTER_SITES=	PYPI
DISTNAME=	${PORTNAME:S/-/_/g}-${DISTVERSION}

MAINTAINER=	5124298+joshiggins@users.noreply.github.com
COMMENT=	Bhyve compute driver for OpenStack Nova
WWW=		https://github.com/stackbsd/nova-bhyve

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}uv-build>=0.11.28:devel/py-uv-build@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>0:devel/py-wheel@${PY_FLAVOR} \
		openstack-runtime>=2026.1.0:net/openstack-runtime

RUN_DEPENDS=	${LOCALBASE}/share/edk2-bhyve/BHYVE_UEFI_CODE.fd:sysutils/edk2@bhyve \
		openstack-nova>=33.0.2:net/openstack-nova \
		openstack-runtime>=2026.1.0:net/openstack-runtime \
		os-brick-freebsd>=0.9.0:net/os-brick-freebsd \
		qemu-img:emulators/qemu@tools

USES=		python:3.12 shebangfix
USE_PYTHON=	noflavors pep517
SHEBANG_GLOB=	*.py
python_CMD=	${VENV}/bin/python${PYTHON_VER}

NO_ARCH=	yes

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
