Summary:	The YubiKey Validation Server
Summary(pl.UTF-8):	Serwer sprawdzający hasła YubiKey
Name:		yubikey-val
Version:	2.41
Release:	1
License:	BSD
Group:		Applications/System
Source0:	https://developers.yubico.com/yubikey-val/Releases/%{name}-%{version}.tgz
# Source0-md5:	e0e42fd82db5c70db3d04ec569342045
Patch0:		%{name}-Makefile.patch
URL:		https://developers.yubico.com/yubikey-val/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core)
Requires:	php(curl)
Requires:	php(mcrypt)
Requires:	php(pdo)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_pear	ykval-.*

%description
This is a server that validates Yubikey OTPs. It is written in PHP,
for use with web servers such as Apache.

%description -l pl.UTF-8
Ten pakiet zawiera serwer sprawdający poprawność OTP Yubikey. Jest
napisany w PHP, przeznaczony do używania z serwerami WWW, takimi jak
Apache.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	etcprefix=$RPM_BUILD_ROOT%{_sysconfdir}/ykval \
	binprefix=$RPM_BUILD_ROOT%{_bindir} \
	sbinprefix=$RPM_BUILD_ROOT%{_sbindir} \
	phpprefix=$RPM_BUILD_ROOT%{_datadir}/ykval \
	manprefix=$RPM_BUILD_ROOT%{_mandir}/man1 \
	docprefix=$RPM_BUILD_ROOT%{_docdir}/ykval \
	muninprefix=$RPM_BUILD_ROOT%{_datadir}/munin/plugins

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README doc/*.adoc ykval-db.sql
%dir %{_sysconfdir}/ykval
%config(noreplace) %{_sysconfdir}/ykval/ykval-config.php
%attr(755,root,root) %{_sbindir}/ykval-*
%{_datadir}/ykval
%{_mandir}/man1/ykval-*.1*

#TODO: subpackage?
#%{_datadir}/munin/plugins/ykval_*
