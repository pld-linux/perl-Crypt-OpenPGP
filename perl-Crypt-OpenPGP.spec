
# Conditional build:
%bcond_with	tests	# perform "make test"

%define		pdir	Crypt
%define		pnam	OpenPGP
Summary:	Crypt::OpenPGP Perl module - pure Perl implementation of the OpenPGP standard
Summary(pl.UTF-8):	Moduł Perla Crypt::OpenPGP - czysto perlowa implementacja standardu OpenPGP
Name:		perl-Crypt-OpenPGP
Version:	1.12
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ab55adcc68487b36d8146fa6081f9997
Patch0:		%{name}-openssl.patch
URL:		http://search.cpan.org/dist/Crypt-OpenPGP/
BuildRequires:	perl-Crypt-DSA
BuildRequires:	perl-Crypt-RSA
BuildRequires:	perl-Data-Buffer >= 0.04
BuildRequires:	perl-Math-Pari
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-Crypt-CAST5_PP
BuildRequires:	perl-Crypt-DES_EDE3
BuildRequires:	perl-Crypt-IDEA
BuildRequires:	perl-Crypt-RIPEMD160
BuildRequires:	perl-Crypt-Rijndael
BuildRequires:	perl-Crypt-Twofish >= 2.00
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-IO-Compress
BuildRequires:	perl-MIME-Base64
%endif
Requires:	perl-Data-Buffer >= 0.04
Requires:	perl-Term-ReadKey
Conflicts:	perl-Crypt-Twofish < 2.00
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is Crypt::OpenPGP. It provides a pure-Perl implementation of the
OpenPGP standard, including support for all versions of PGP and GnuPG.
It needs at least one simmetric cipher Perl module (Crypt::DES_EDE3
for 3DES, Crypt::CAST5_PP for CAST5, Crypt::IDEA for IDEA,
Crypt::Blowfish for Blowfish, Crypt::Twofish >= 2.00 for Twofish or
Crypt;:Rijndael for Rijndael) and at least one digest Perl module
(Digest::MD5 for MD5, Digest::SHA1 for SHA1 or Crypt::RIPEMD160 for
RIPE-MD/160).

%description -l pl.UTF-8
To jest moduł Crypt::OpenPGP. Jest on czysto perlową implementacją
standardu OpenPGP, wraz ze wsparciem dla wszystkich wersji PGP i
GnuPG. Wymaga co najmniej jednego modułu Perla z implementacją szyfru
symetrycznego (Crypt::DES_EDE3 dla 3DES, Crypt::CAST5_PP dla CAST5,
Crypt::IDEA dla szyfru IDEA, Crypt::Blowfish dla szyfru Blowfish,
Crypt::Twofish >= 2.00 dla szyfru Twofish albo Crypt::Rijndale dla
szyfru Rijndael) oraz co najmniej jednego modułu z implementacją
funkcji skrótu (Digest::MD5 dla MD5, Digest::SHA1 dla SHA1 albo
Crypt::RIPEMD160 dla RIPE-MD/160).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pgplet
%doc Changes README
%{perl_vendorlib}/Crypt/OpenPGP.pm
%{perl_vendorlib}/Crypt/OpenPGP
%{_mandir}/man3/*
