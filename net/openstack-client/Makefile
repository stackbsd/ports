PORTNAME=	client
DISTVERSION=	9.0.0
CATEGORIES=	net python
PKGNAMEPREFIX=	openstack-

MAINTAINER=	5124298+joshiggins@users.noreply.github.com
COMMENT=	OpenStack Client
WWW=		https://docs.openstack.org/python-openstackclient/

LICENSE=	APACHE20

BUILD_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime

RUN_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime

NO_ARCH=	yes

PLIST_SUB=	VENV=libexec/openstack

# the distfile set and the wheel engine shared with the other openstack ports
.include "${.CURDIR}/../openstack-runtime/Makefile.venv"

do-install:
	${SETENV} PYTHONPATH=${PYTHON_SITELIBDIR} \
		${LOCALBASE}/libexec/openstack/bin/python${PYTHON_VER} -m installer \
		--destdir ${STAGEDIR} --prefix ${VENV} --no-compile-bytecode \
		${WHEELDIR}/*.whl

post-install:
	@${MKDIR} ${STAGEDIR}${PREFIX}/bin
	${RLN} ${STAGEDIR}${VENV}/bin/openstack ${STAGEDIR}${PREFIX}/bin/openstack

.include <bsd.port.mk>
