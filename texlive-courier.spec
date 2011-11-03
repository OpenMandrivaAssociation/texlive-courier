# revision 21993
# category Package
# catalog-ctan /fonts/urw/base35
# catalog-date 2011-03-01 21:42:17 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-courier
Version:	20110301
Release:	1
Summary:	URW "Base 35" font pack for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/urw/base35
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courier.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/courier/config.ucr
%{_texmfdistdir}/fonts/afm/adobe/courier/pcrb8a.afm
%{_texmfdistdir}/fonts/afm/adobe/courier/pcrbo8a.afm
%{_texmfdistdir}/fonts/afm/adobe/courier/pcrr8a.afm
%{_texmfdistdir}/fonts/afm/adobe/courier/pcrro8a.afm
%{_texmfdistdir}/fonts/afm/ibm/courier/cour.afm
%{_texmfdistdir}/fonts/afm/ibm/courier/courb.afm
%{_texmfdistdir}/fonts/afm/ibm/courier/courbi.afm
%{_texmfdistdir}/fonts/afm/ibm/courier/couri.afm
%{_texmfdistdir}/fonts/afm/ibm/courier/cr-pc8.afm
%{_texmfdistdir}/fonts/afm/ibm/courier/crb-pc8.afm
%{_texmfdistdir}/fonts/afm/ibm/courier/crbi-pc8.afm
%{_texmfdistdir}/fonts/afm/ibm/courier/cri-pc8.afm
%{_texmfdistdir}/fonts/afm/urw/courier/ucrb8a.afm
%{_texmfdistdir}/fonts/afm/urw/courier/ucrbo8a.afm
%{_texmfdistdir}/fonts/afm/urw/courier/ucrr8a.afm
%{_texmfdistdir}/fonts/afm/urw/courier/ucrro8a.afm
%{_texmfdistdir}/fonts/map/dvips/courier/ucr.map
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrb.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrb7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrb8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrb8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrb8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrbc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrbc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrbc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrbo.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrbo7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrbo8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrbo8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrbo8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrr.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrr7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrr8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrr8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrr8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrrc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrrc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrrc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrro.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrro7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrro8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrro8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/courier/pcrro8t.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/ccrb.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/ccrb8t.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/ccrbi.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/ccrbi8t.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/ccrr.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/ccrr8t.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/ccrri.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/ccrri8t.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crb10u.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crb2n.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crb6j.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crb7j.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crb8u.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crb9t.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/cri10u.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/cri2n.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/cri6j.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/cri7j.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/cri8u.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/cri9t.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crj10u.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crj2n.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crj6j.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crj7j.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crj8u.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crj9t.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crr10u.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crr2n.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crr6j.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crr7j.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crr8u.tfm
%{_texmfdistdir}/fonts/tfm/cg/courier/crr9t.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/courier/pcrb8u.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/courier/pcrbc8u.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/courier/pcrbo8u.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/courier/pcrr8u.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/courier/pcrrc8u.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/courier/pcrro8u.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/courier/rpcrb.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/courier/rpcrbo.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/courier/rpcrr.tfm
%{_texmfdistdir}/fonts/tfm/cspsfonts-adobe/courier/rpcrro.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrb7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrb8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrb8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrb8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrbc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrbc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrbo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrbo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrbo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrbo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrr7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrr8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrr8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrr8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrrc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrrc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrro7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrro8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrro8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/courier/ucrro8t.tfm
%{_texmfdistdir}/fonts/type1/adobe/courier/pcrb8a.pfb
%{_texmfdistdir}/fonts/type1/adobe/courier/pcrbi8a.pfb
%{_texmfdistdir}/fonts/type1/adobe/courier/pcrbo8a.pfb
%{_texmfdistdir}/fonts/type1/adobe/courier/pcri8a.pfb
%{_texmfdistdir}/fonts/type1/adobe/courier/pcrr8a.pfb
%{_texmfdistdir}/fonts/type1/adobe/courier/pcrro8a.pfb
%{_texmfdistdir}/fonts/type1/urw/courier/ucrb8a.pfb
%{_texmfdistdir}/fonts/type1/urw/courier/ucrb8a.pfm
%{_texmfdistdir}/fonts/type1/urw/courier/ucrbo8a.pfb
%{_texmfdistdir}/fonts/type1/urw/courier/ucrbo8a.pfm
%{_texmfdistdir}/fonts/type1/urw/courier/ucrr8a.pfb
%{_texmfdistdir}/fonts/type1/urw/courier/ucrr8a.pfm
%{_texmfdistdir}/fonts/type1/urw/courier/ucrro8a.pfb
%{_texmfdistdir}/fonts/type1/urw/courier/ucrro8a.pfm
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrb.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrb7t.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrb8c.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrb8t.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrbc.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrbc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrbc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrbo.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrbo7t.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrbo8c.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrbo8t.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrr.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrr7t.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrr8c.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrr8t.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrrc.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrrc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrrc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrro.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrro7t.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrro8c.vf
%{_texmfdistdir}/fonts/vf/adobe/courier/pcrro8t.vf
%{_texmfdistdir}/fonts/vf/cg/courier/ccrb.vf
%{_texmfdistdir}/fonts/vf/cg/courier/ccrb8t.vf
%{_texmfdistdir}/fonts/vf/cg/courier/ccrbi.vf
%{_texmfdistdir}/fonts/vf/cg/courier/ccrbi8t.vf
%{_texmfdistdir}/fonts/vf/cg/courier/ccrr.vf
%{_texmfdistdir}/fonts/vf/cg/courier/ccrr8t.vf
%{_texmfdistdir}/fonts/vf/cg/courier/ccrri.vf
%{_texmfdistdir}/fonts/vf/cg/courier/ccrri8t.vf
%{_texmfdistdir}/fonts/vf/cspsfonts-adobe/courier/pcrb8u.vf
%{_texmfdistdir}/fonts/vf/cspsfonts-adobe/courier/pcrbc8u.vf
%{_texmfdistdir}/fonts/vf/cspsfonts-adobe/courier/pcrbo8u.vf
%{_texmfdistdir}/fonts/vf/cspsfonts-adobe/courier/pcrr8u.vf
%{_texmfdistdir}/fonts/vf/cspsfonts-adobe/courier/pcrrc8u.vf
%{_texmfdistdir}/fonts/vf/cspsfonts-adobe/courier/pcrro8u.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrb7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrb8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrb8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrbc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrbc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrbo7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrbo8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrbo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrr7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrr8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrr8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrrc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrrc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrro7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrro8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/courier/ucrro8t.vf
%{_texmfdistdir}/tex/latex/courier/8rucr.fd
%{_texmfdistdir}/tex/latex/courier/omlucr.fd
%{_texmfdistdir}/tex/latex/courier/omsucr.fd
%{_texmfdistdir}/tex/latex/courier/ot1ucr.fd
%{_texmfdistdir}/tex/latex/courier/t1ucr.fd
%{_texmfdistdir}/tex/latex/courier/ts1ucr.fd
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
