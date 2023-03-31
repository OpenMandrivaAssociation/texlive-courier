Name:		texlive-courier
Version:	61719
Release:	2
Summary:	URW "Base 35" font pack for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/urw/base35
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courier.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: - Century Schoolbook (substituting for
Adobe's New Century Schoolbook); - Dingbats (substituting for
Adobe's Zapf Dingbats); - Nimbus Mono L (substituting for
Abobe's Courier); - Nimbus Roman No9 L (substituting for
Adobe's Times); - Nimbus Sans L (substituting for Adobe's
Helvetica); - Standard Symbols L (substituting for Adobe's
Symbol); - URW Bookman; - URW Chancery L Medium Italic
(substituting for Adobe's Zapf Chancery); - URW Gothic L Book
(substituting for Adobe's Avant Garde); and - URW Palladio L
(substituting for Adobe's Palatino).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/courier
%{_texmfdistdir}/fonts/afm/adobe/courier
%{_texmfdistdir}/fonts/afm/urw/courier
%{_texmfdistdir}/fonts/map/dvips/courier
%{_texmfdistdir}/fonts/tfm/adobe/courier
%{_texmfdistdir}/fonts/tfm/urw35vf/courier
%{_texmfdistdir}/fonts/type1/adobe/courier
%{_texmfdistdir}/fonts/type1/urw/courier
%{_texmfdistdir}/fonts/vf/adobe/courier
%{_texmfdistdir}/fonts/vf/urw35vf/courier
%{_texmfdistdir}/tex/latex/courier

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex %{buildroot}%{_texmfdistdir}
