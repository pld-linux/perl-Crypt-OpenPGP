#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenPGP
Summary:	Crypt::OpenPGP Perl module - pure Perl implementation of the OpenPGP standard
Summary(pl):	Modu³ Perla Crypt::OpenPGP - czysto perlowa implementacja standardu OpenPGP
Name:		perl-Crypt-OpenPGP
Version:	1.02
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-nonint.patch
Patch1:		%{name}-noautodownload.patch
BuildRequires:	perl >= 5.6
%{!?_without_tests:BuildRequires:	perl-Compress-Zlib}
%{!?_without_tests:BuildRequires:	perl-Crypt-Blowfish}
%{!?_without_tests:BuildRequires:	perl-Crypt-CAST5_PP}
%{!?_without_tests:BuildRequires:	perl-Crypt-DES_EDE3}
%{!?_without_tests:BuildRequires:	perl-Crypt-DSA}
%{!?_without_tests:BuildRequires:	perl-Crypt-IDEA}
%{!?_without_tests:BuildRequires:	perl-Crypt-RIPEMD160}
%{!?_without_tests:BuildRequires:	perl-Crypt-RSA}
%{!?_without_tests:BuildRequires:	perl-Crypt-Rijndael}
%{!?_without_tests:BuildRequires:	perl-Crypt-Twofish >= 2.00}
%{!?_without_tests:BuildRequires:	perl-Data-Buffer >= 0.04}
%{!?_without_tests:BuildRequires:	perl-Digest-MD5}
%{!?_without_tests:BuildRequires:	perl-Digest-SHA1}
%{!?_without_tests:BuildRequires:	perl-MIME-Base64}
%{!?_without_tests:BuildRequires:	perl-Math-Pari}
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	perl-Crypt-DSA
Requires:	perl-Crypt-RIPEMD160
Requires:	perl-Crypt-RSA
Requires:	perl-Data-Buffer >= 0.04
Requires:	perl-Term-ReadKey
Requires:	perl-libwww
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
GnuPG. Wymaga co najmniej jednego modu³u Perla z implementacj±
szyfru symetrycznego (Crypt::DES_EDE3 dla 3DES, Crypt::CAST5_PP dla
CAST5, Crypt::IDEA dla szyfru IDEA, Crypt::Blowfish dla szyfru
Blowfish, Crypt::Twofish >= 2.00 dla szyfru Twofish albo
Crypt::Rijndale dla szyfru Rijndael) oraz co najmniej jednego modu³u z
implementacj± funkcji skrótu (Digest::MD5 dla MD5, Digest::SHA1 dla
SHA1 albo Crypt::RIPEMD160 dla RIPE-MD/160).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p1

%build
perl Makefile.PL </dev/null
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%{perl_sitelib}/Crypt/OpenPGP.pm
%{perl_sitelib}/Crypt/OpenPGP
%{_mandir}/man3/*
