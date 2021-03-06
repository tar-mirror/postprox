Summary: Minimal Postfix SMTP proxy
Name: postprox
Version: 0.2.0
Release: 1
License: Artistic
Group: Development/Tools
Source: http://www.ivarch.com/programs/sources/postprox-0.2.0.tar.bz2
BuildRoot: /var/tmp/%{name}-%{version}-root
Provides: postprox = 0.2.0-1

%description
The minimal Postfix SMTP proxy copies an SMTP conversation between its input
and another SMTP server, but spools the DATA portion to a temporary file and
runs a specified program on it before passing it on to the output server -
or outputting an SMTP error code instead if the content filter says so.

%prep
%setup -n postprox-0.2.0
CFLAGS="$RPM_OPT_FLAGS" sh ./configure \
%if %{?_with_static:1}0
  --enable-static \
%endif
  --enable-debugging \
  --prefix=/usr \
  --infodir=/usr/share/info \
  --mandir=/usr/share/man \
  --sysconfdir=/etc

%build
make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
[ -e "$RPM_BUILD_ROOT" ] || mkdir -m 755 "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"
chmod 755 "$RPM_BUILD_ROOT"/usr/sbin/postprox*

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"

%pre

%post
chmod 755 /usr/share/doc/postprox-%{version}/*.sh 2>/dev/null || :
chmod 755 /usr/share/doc/postprox-%{version}/*.pl 2>/dev/null || :

%preun

%postun

%files
%defattr(-, root, root)
/usr/sbin/postprox
%docdir /usr/share/man/man1
/usr/share/man/man1/*
%doc README doc/NEWS doc/TODO doc/COPYING extra/*.sh

%changelog
* Tue Jan 24 2006 Andrew Wood <andrew.wood@ivarch.com>
- Added capability for filtering scripts to modify the email in transit.
- Capture IP address, HELO, sender/recipient for logging and for filter scripts.

* Fri Aug  5 2005 Andrew Wood <andrew.wood@ivarch.com>
- First draft of spec file created
