%define upstream_name	 MIME-tools
%define upstream_version 5.502

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4
Summary:	Perl modules for parsing (and creating!) MIME entities
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MIME/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(File::Temp)   >= 0.17
BuildRequires:	perl(IO::Stringy)  >= 1.211
BuildRequires:	perl(Mail::Util)   >= 1.15
BuildRequires:	perl(MIME::Base64) >= 3.03
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl-devel
Requires:   perl(File::Temp)   >= 0.17
Requires:	perl(IO::Stringy)  >= 1.211
Requires:	perl(MIME::Base64) >= 3.03
Requires:	perl(Mail::Util)   >= 1.15
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 5.502.0-4mdv2012.0
+ Revision: 765484
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 5.502.0-2
+ Revision: 667244
- mass rebuild

* Tue Mar 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 5.502.0-1
+ Revision: 644906
- update to new version 5.502

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 5.428.0-2mdv2011.0
+ Revision: 555303
- rebuild

* Fri Apr 23 2010 Jérôme Quelin <jquelin@mandriva.org> 5.428.0-1mdv2010.1
+ Revision: 538299
- update to 5.428

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 5.427-2mdv2010.0
+ Revision: 426519
- rebuild

* Tue Jul 01 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.427-1mdv2009.0
+ Revision: 230452
- update to new version 5.427

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.426-1mdv2009.0
+ Revision: 194934
- update to new version 5.426

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 15 2007 Olivier Thauvin <nanardon@mandriva.org> 5.425-2mdv2008.1
+ Revision: 120276
- require perl(File::Temp) to fix 36010 (thx Berthy)

* Wed Nov 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.425-1mdv2008.1
+ Revision: 110920
- update to new version 5.425

  + Funda Wang <fwang@mandriva.org>
    - fix source tarball url

* Sun Apr 29 2007 Olivier Thauvin <nanardon@mandriva.org> 5.420-2mdv2008.0
+ Revision: 19200
- rebuild


* Mon Mar 20 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.420-1mdk
- 5.420

* Thu Dec 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.419-1mdk
- 5.419

* Mon Oct 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.418-1mdk
- 5.418

* Sat Jan 29 2005 Guillaume Rousse <guillomovitch@mandrake.org> 5.417-1mdk 
- new version
- spec cleanup

* Fri Jan 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.416-1mdk
- 5.416

* Tue Nov 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.415-1mdk
- New version 5.415
- Update dependency on MIME::Base64

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.411-7mdk
- own dir
- rebuild

* Wed Aug 13 2003 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 5.411-6mdk
- rebuild against new perl
- drop Prefix tag
- drop $RPM_OPT_FLAGS, noarch..
- don't use PREFIX
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.411-5mdk
- rebuild for new auto{prov,req}

