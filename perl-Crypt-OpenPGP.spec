
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenPGP
Summary:	Crypt::OpenPGP Perl module - pure Perl implementation of the OpenPGP standard
Summary(pl):	Modu³ Perla Crypt::OpenPGP - czysto perlowa implementacja standardu OpenPGP
Name:		perl-Crypt-OpenPGP
Version:	1.03
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	020141cf2a3c22b50373fc5aeb7914d2
BuildRequires:	perl-Crypt-DSA
BuildRequires:	perl-Crypt-RSA
BuildRequires:	perl-Data-Buffer >= 0.04
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Math-Pari
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-Crypt-CAST5_PP
BuildRequires:	perl-Crypt-DES_EDE3
BuildRequires:	perl-Crypt-IDEA
BuildRequires:	perl-Crypt-RIPEMD160
BuildRequires:	perl-Crypt-Rijndael
BuildRequires:	perl-Crypt-Twofish >= 2.00
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-Digest-SHA1
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

%description -l pl
To jest modu³ Crypt::OpenPGP. Jest on czysto perlow± implementacj±
standardu OpenPGP, wraz ze wsparciem dla wszystkich wersji PGP i
GnuPG. Wymaga co najmniej jednego modu³u Perla z implementacj± szyfru
symetrycznego (Crypt::DES_EDE3 dla 3DES, Crypt::CAST5_PP dla CAST5,
Crypt::IDEA dla szyfru IDEA, Crypt::Blowfish dla szyfru Blowfish,
Crypt::Twofish >= 2.00 dla szyfru Twofish albo Crypt::Rijndale dla
szyfru Rijndael) oraz co najmniej jednego modu³u z implementacj±
funkcji skrótu (Digest::MD5 dla MD5, Digest::SHA1 dla SHA1 albo
Crypt::RIPEMD160 dla RIPE-MD/160).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes README ToDo
%{perl_vendorlib}/Crypt/OpenPGP.pm
%{perl_vendorlib}/Crypt/OpenPGP
%{_mandir}/man3/*
