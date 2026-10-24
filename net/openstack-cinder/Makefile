PORTNAME=	cinder
DISTVERSION=	28.0.0
CATEGORIES=	net python
PKGNAMEPREFIX=	openstack-

MAINTAINER=	josh@joshh.info
COMMENT=	OpenStack Block Storage service (Cinder)
WWW=		https://docs.openstack.org/cinder/

LICENSE=	APACHE20

BUILD_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime

RUN_DEPENDS=	openstack-runtime>=2026.1.0:net/openstack-runtime \
		qemu-img:emulators/qemu@tools \
		sudo:security/sudo

USE_RC_SUBR=	cinder-api cinder-scheduler cinder-volume

SUB_FILES=	cinder-api.sh cinder-manage.sh cinder-rootwrap.sh \
		cinder-scheduler.sh cinder-status.sh cinder-volume.sh \
		cinder.conf rootwrap.conf sudoers
SUB_LIST=	VENV=${VENV}

USERS=		cinder
GROUPS=		cinder

PLIST_SUB=	VENV=libexec/openstack

# the distfile set and the wheel engine shared with the other openstack ports
.include "${.CURDIR}/../openstack-runtime/Makefile.venv"

do-install:
	${SETENV} PYTHONPATH=${PYTHON_SITELIBDIR} \
		${LOCALBASE}/libexec/openstack/bin/python${PYTHON_VER} -m installer \
		--destdir ${STAGEDIR} --prefix ${VENV} --no-compile-bytecode \
		${WHEELDIR}/*.whl

post-install:
	${INSTALL_SCRIPT} ${WRKDIR}/cinder-api.sh ${STAGEDIR}${PREFIX}/bin/cinder-api
	${INSTALL_SCRIPT} ${WRKDIR}/cinder-manage.sh ${STAGEDIR}${PREFIX}/bin/cinder-manage
	${INSTALL_SCRIPT} ${WRKDIR}/cinder-rootwrap.sh ${STAGEDIR}${PREFIX}/bin/cinder-rootwrap
	${INSTALL_SCRIPT} ${WRKDIR}/cinder-scheduler.sh ${STAGEDIR}${PREFIX}/bin/cinder-scheduler
	${INSTALL_SCRIPT} ${WRKDIR}/cinder-status.sh ${STAGEDIR}${PREFIX}/bin/cinder-status
	${INSTALL_SCRIPT} ${WRKDIR}/cinder-volume.sh ${STAGEDIR}${PREFIX}/bin/cinder-volume
	@${MKDIR} ${STAGEDIR}${ETCDIR} ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d \
		${STAGEDIR}${PREFIX}/etc/sudoers.d
	${INSTALL_DATA} ${WRKDIR}/cinder.conf ${STAGEDIR}${ETCDIR}/cinder.conf.sample
	${INSTALL_DATA} ${FILESDIR}/cinder-wsgi.conf ${STAGEDIR}${ETCDIR}/cinder-wsgi.conf.sample
	${INSTALL_DATA} ${WRKDIR}/rootwrap.conf ${STAGEDIR}${ETCDIR}/rootwrap.conf.sample
	${INSTALL_DATA} ${STAGEDIR}${VENV}/etc/cinder/api-paste.ini ${STAGEDIR}${ETCDIR}
	${INSTALL_DATA} ${STAGEDIR}${VENV}/etc/cinder/resource_filters.json ${STAGEDIR}${ETCDIR}
	${INSTALL_DATA} ${WRKDIR}/sudoers ${STAGEDIR}${PREFIX}/etc/sudoers.d/openstack-cinder
	${INSTALL_DATA} ${FILESDIR}/cinder-log.conf ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d

.include <bsd.port.mk>
