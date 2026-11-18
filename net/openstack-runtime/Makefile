PORTNAME=	runtime
CATEGORIES=	net python
PKGNAMEPREFIX=	openstack-

MAINTAINER=	josh@joshh.info
COMMENT=	Shared Python runtime virtual environment for the OpenStack services
WWW=		https://github.com/stackbsd

LICENSE=	APACHE20

LIB_DEPENDS=	libffi.so:devel/libffi \
		libopenblas.so:math/openblas \
		libxml2.so:textproc/libxml2 \
		libxslt.so:textproc/libxslt \
		libyaml.so:textproc/libyaml

PLIST_SUB=	VENV=libexec/openstack

# the distfile set and the wheel engine shared with the service ports
.include "${.CURDIR}/Makefile.venv"

do-install:
	${PYTHON_CMD} -m venv ${STAGEDIR}${VENV}
	${STAGEDIR}${VENV}/bin/pip install --no-index --no-deps \
		--no-compile ${WHEELDIR}/*.whl

post-install:
	${RM} ${STAGEDIR}${VENV}/bin/activate* ${STAGEDIR}${VENV}/bin/Activate.ps1
	${REINPLACE_CMD} -e "s|${STAGEDIR}||" ${STAGEDIR}${VENV}/pyvenv.cfg

.include <bsd.port.mk>
