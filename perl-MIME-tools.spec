%define module	MIME-tools
%define name	perl-%{module}
%define version	5.420
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl modules for parsing (and creating!) MIME entities
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/authors/id/D/DS/DSKOLL/%{module}-%{version}.tar.bz2
Requires:	perl-IO-stringy >= 1.211
Requires:	perl-MailTools >= 1.15
Requires:	perl(MIME::Base64) >= 3.03
BuildRequires:	perl-devel
BuildRequires:	perl-IO-stringy >= 1.211
BuildRequires:	perl-MailTools >= 1.15
BuildRequires:	perl(MIME::Base64) >= 3.03
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
MIME-tools - modules for parsing (and creating!) MIME entities Modules in this
toolkit : Abstract message holder (file, scalar, etc.), OO interface for
decoding MIME messages, an extracted and decoded MIME entity, Mail::Field
subclasses for parsing fields, a parsed MIME header (Mail::Header subclass),
parser and tool for building your own MIME parser, and utilities.

%prep
%setup -q -n %{module}-%{version}

%build
rm -f set-version.pl
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std 
%{__chmod} 0644 %{buildroot}%{_mandir}/*/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog
%{perl_vendorlib}/MIME
%{_mandir}/*/*

