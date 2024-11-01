%define modname	MIME-tools

Summary:	Perl modules for parsing (and creating!) MIME entities
Name:		perl-%{modname}
Version:	5.515
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/pod/MIME::Tools
Source0:	https://cpan.metacpan.org/authors/id/D/DS/DSKOLL/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(File::Temp)   >= 0.17
BuildRequires:	perl(IO::Stringy)  >= 1.211
BuildRequires:	perl(Mail::Util)   >= 1.15
BuildRequires:	perl(MIME::Base64) >= 3.03
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
Requires:	perl(File::Temp)   >= 0.17
Requires:	perl(IO::Stringy)  >= 1.211
Requires:	perl(MIME::Base64) >= 3.03
Requires:	perl(Mail::Util)   >= 1.15

%description
MIME-tools - modules for parsing (and creating!) MIME entities Modules in this
toolkit :	Abstract message holder (file, scalar, etc.), OO interface for
decoding MIME messages, an extracted and decoded MIME entity, Mail::Field
subclasses for parsing fields, a parsed MIME header (Mail::Header subclass),
parser and tool for building your own MIME parser, and utilities.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
rm -f set-version.pl
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make_build test

%install
%make_install

%files
%doc README COPYING ChangeLog
%{perl_vendorlib}/MIME
%{_mandir}/man3/*
