Summary:	The Dink Smallwood game engine
Summary(pl.UTF-8):	Silnik gry Dink Smallwood
Name:		freedink
Version:	1.08.20100321
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://ftp.gnu.org/gnu/freedink/%{name}-%{version}.tar.gz
# Source0-md5:	3d1f3507bf3099bdb0bb609eb72d2eab
Patch0:		%{name}-desktop.patch
URL:		http://www.freedink.org/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	gettext-devel
BuildRequires:	help2man
BuildRequires:	pkgconfig
BuildRequires:	zip
BuildRequires:	zlib-devel
BuildRequires:	zziplib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeDink is a portable and enhanced version of the Dink Smallwood game
engine.

It still needs some data files from the orginal game.

%description -l pl.UTF-8
FreeDink jest przenośną i ulepszoną wersją silnika gry Dink Smallwood.

Do uruchomienia wymagane są pliki z oryginalnej werjsji gry.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I gnulib/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TROUBLESHOOTING doc/TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man6/*.6*
%{_pixmapsdir}/freedink.png
