%include	/usr/lib/rpm/macros.php
Summary:	The YubiKey Validation Server
Name:		yubikey-val
Version:	2.10
Release:	0.1
License:	BSD
Group:		Applications/System
# FIXME: no source0
Source0:	http://yubikey-val-server-php.googlecode.com/files/%{name}-%{version}.tgz
URL:		http://code.google.com/p/yubikey-val-server-php/
Patch0:		%{name}-Makefile.patch
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core)
Requires:	php(curl)
Requires:	php(mcrypt)
Requires:	php(pdo)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a server that validates Yubikey OTPs. It is written in PHP,
for use with web servers such as Apache

%prep
%setup -q
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	etcprefix=$RPM_BUILD_ROOT%{_sysconfdir}/ykval \
	binprefix=$RPM_BUILD_ROOT%{_bindir} \
	sbinprefix=$RPM_BUILD_ROOT%{_sbindir} \
	phpprefix=$RPM_BUILD_ROOT%{_datadir}/ykval \
	docprefix=$RPM_BUILD_ROOT%{_docdir}/ykval \
	muninprefix=$RPM_BUILD_ROOT%{_datadir}/munin/plugins

rm -r $RPM_BUILD_ROOT%{_docdir}
mv $RPM_BUILD_ROOT%{_sysconfdir}/ykval/ykval-config.php-template $RPM_BUILD_ROOT%{_sysconfdir}/ykval/ykval-config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* ykval-db.sql
%dir %{_sysconfdir}/ykval
%config(noreplace) %{_sysconfdir}/ykval/ykval-config.php
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/ykval
