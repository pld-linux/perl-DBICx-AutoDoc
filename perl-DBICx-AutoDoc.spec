#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	DBICx
%define	pnam	AutoDoc
%include	/usr/lib/rpm/macros.perl
Summary:	DBICx::AutoDoc - Generate automatic documentation of DBIx::Class::Schema objects
Summary(pl.UTF-8):	DBICx::AutoDoc - generuje automatycznie dokumentacje objektów DBIx::Class::Schema
Name:		perl-DBICx-AutoDoc
Version:	0.07
Release:	3
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JA/JASONK/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e994f640728fc9f9a3727237dd63731d
URL:		http://search.cpan.org/dist/DBICx-AutoDoc/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor-Grouped
BuildRequires:	perl-Class-Inspector
BuildRequires:	perl-DBIx-Class
BuildRequires:	perl-Data-Dump
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-Template-Toolkit
BuildRequires:	perl-Tie-IxHash
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBICx::AutoDoc is a utility that can automatically generate
documentation for your DBIx::Class schemas. It works by collecting
information from several sources and arranging it into a format that
makes it easier to deal with from templates.

%description -l pl.UTF-8
DBICx::AutoDoc jest narzędziem, które potrafi automatycznie generować
dokumentację dla wzorców DBIx::Class.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/dbicx-autodoc
%dir %{perl_vendorlib}/DBICx
%{perl_vendorlib}/DBICx/*.pm
%dir %{perl_vendorlib}/DBICx/AutoDoc
%{perl_vendorlib}/DBICx/AutoDoc/*pm
%dir %{perl_vendorlib}/auto/share/dist/DBICx-AutoDoc
%{perl_vendorlib}/auto/share/dist/DBICx-AutoDoc/*tt2
%{perl_vendorlib}/auto/share/dist/DBICx-AutoDoc/AUTODOC*
%{perl_vendorlib}/auto/share/dist/DBICx-AutoDoc/*css
%{_mandir}/man3/*
%{_mandir}/man1/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
