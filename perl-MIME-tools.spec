%define upstream_name	 MIME-tools
%define upstream_version 5.428

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl modules for parsing (and creating!) MIME entities
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MIME/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(File::Temp)   >= 0.17
BuildRequires:	perl(IO::Stringy)  >= 1.211
BuildRequires:	perl(Mail::Util)   >= 1.15
BuildRequires:	perl(MIME::Base64) >= 3.03

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:   perl(File::Temp)   >= 0.17
Requires:	perl(IO::Stringy)  >= 1.211
Requires:	perl(MIME::Base64) >= 3.03
Requires:	perl(Mail::Util)   >= 1.15

%description
MIME-tools - modules for parsing (and creating!) MIME entities Modules in this
toolkit : Abstract message holder (file, scalar, etc.), OO interface for
decoding MIME messages, an extracted and decoded MIME entity, Mail::Field
subclasses for parsing fields, a parsed MIME header (Mail::Header subclass),
parser and tool for building your own MIME parser, and utilities.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
rm -f set-version.pl
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std 

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog
%{perl_vendorlib}/MIME
%{_mandir}/*/*
