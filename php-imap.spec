%define _disable_ld_no_undefined 1

Name: php-imap
Version: 1.0.3
Release: 1
Source0: https://pecl.php.net/get/imap-%{version}.tgz
Summary: PHP extension to use the IMAP, NNTP and POP3 protocols and access local mailboxes
URL: https://pecl.php.net/package/imap
# See also https://github.com/php/pecl-mail-imap
License: PHP
Group: Servers
# php-imap used to be bundled with php, giving it version
# numbers up to 8.3.x (it was dropped in 8.4)
Obsoletes: php-imap > 5.0
BuildRequires: php-devel
BuildRequires: c-client-devel
BuildRequires: pkgconfig(openssl)

%description
PHP extension to use the IMAP, NNTP and POP3 protocols and access local mailboxes

%prep
%autosetup -p1 -n imap-%{version}

%conf
phpize
if ! %configure --with-libdir=%{_lib}; then
	cat config.log
fi

%build
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/php.d
echo 'extension = imap.so' >%{buildroot}%{_sysconfdir}/php.d/27_imap.ini

%files
%{_sysconfdir}/php.d/27_imap.ini
%{_libdir}/php/extensions/imap.so
