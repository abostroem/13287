PRO PLOTLINES,label=label

lambda=[1240,1394,1403,1483,1488,1549,1551,1640,1661,1666,1747,1753,1815,1883,1892,1906,1909,2322,2329,2802,2896]
names=['N V 1240','Si IV 1394','Si IV 1403','N IV 1483','N IV 1488','C IV 1549','C IV 1551','He II 1640','O III 1661','O III 1666','N III 1747','N III 1753','Ne III 1815','Si III/C III 1883','Si III/C III 1892','Si III/C III 1906','Si III/C III 1909','C II 2322','C II 2329','Mg 2796','Mg 2802']

constant=1.60
charsize=2
orientation=90

FOR i=0,n_elements(lambda)-1 DO BEGIN
   x=[lambda(i),lambda(i)]
   y=[1.d-18,8.d-15]
;   IF cutoff EQ 0 THEN IF lambda(i) LT 4300 OR lambda(i) GT 7000 THEN CONTINUE
;   IF cutoff EQ 1 THEN IF lambda(i) LT 6000 OR lambda(i) GT 10000 THEN CONTINUE
   IF label EQ 1 THEN BEGIN
      IF strcmp(names(i),'Si IV 1403') THEN  xyouts,lambda(i)+10,1.d-15,names(i),orientation=90,charsize=0.5,charthick=3 ELSE $
         IF strcmp(names(i),'N IV 1488') THEN  xyouts,lambda(i)+20,1.d-15,names(i),orientation=90,charsize=0.5,charthick=3 ELSE $
         IF strcmp(names(i),'C IV 1551') THEN  xyouts,lambda(i)+23,1.d-15,names(i),orientation=90,charsize=0.5,charthick=3 ELSE $
         IF strcmp(names(i),'O III 1666') THEN  xyouts,lambda(i)+23,1.d-15,names(i),orientation=90,charsize=0.5,charthick=3 ELSE $
         IF strcmp(names(i),'N III 1753') THEN  xyouts,lambda(i)+23,1.d-15,names(i),orientation=90,charsize=0.5,charthick=3 ELSE $
         IF strcmp(names(i),'Si III/C III 1892') THEN  xyouts,lambda(i)+30,1.d-15,names(i),orientation=90,charsize=0.5,charthick=3 ELSE $
         IF strcmp(names(i),'Si III/C III 1906') THEN  xyouts,lambda(i)+46,1.d-15,names(i),orientation=90,charsize=0.5,charthick=3 ELSE $
         IF strcmp(names(i),'Si III/C III 1909') THEN  xyouts,lambda(i)+66,1.d-15,names(i),orientation=90,charsize=0.5,charthick=3 ELSE $
         IF strcmp(names(i),'C II 2329') THEN  xyouts,lambda(i)+30,1.d-15,names(i),orientation=90,charsize=0.5,charthick=3 ELSE $
         xyouts,lambda(i)+0,1.d-15,names(i),orientation=90,charsize=0.5,charthick=3
      oplot,[lambda(i),lambda(i)],[y(0),1.d-15],thick=3,linestyle=2,color=gray
   ENDIF ELSE BEGIN
      oplot,[lambda(i),lambda(i)],[y(0),y(1)],thick=3,linestyle=2,color=gray   
   ENDELSE
   skiplabels:
ENDFOR

END

;***********************************************************

PRO plotall

fuv_10jl=mrdfits('2010jl_loc_327.0_hgt_21/2010jl_fuv_x1dsum.fits',1,fuv_h_10jl)
fuv_lam_10jl=fuv_10jl.wavelength
fuv_flux_10jl=fuv_10jl.flux

nuv_10jl=mrdfits('2010jl_loc_323.0_hgt_21/2010jl_nuv_x1dsum.fits',1,nuv_h_10jl)
nuv_lam_10jl=nuv_10jl.wavelength
nuv_flux_10jl=nuv_10jl.flux

fuv_05ip=mrdfits('2005ip_otfr/2005ip_fuv_x1dsum.fits',1,fuv_h_05ip)
fuv_lam_05ip=fuv_05ip.wavelength
fuv_flux_05ip=fuv_05ip.flux

fuv_09ip=mrdfits('2009ip_otfr/2009ip_fuv_x1dsum.fits',1,fuv_h_09ip)
fuv_lam_09ip=fuv_09ip.wavelength
fuv_flux_09ip=fuv_09ip.flux

nuv_05ip=mrdfits('2005ip_otfr/2005ip_nuv_x1dsum.fits',1,nuv_05ip)
nuv_lam_05ip=nuv_05ip.wavelength
nuv_flux_05ip=nuv_05ip.flux

stis_spec=mrdfits('sn1998s/sn1998s-19981026.000-hst.fits',1,h)
lam_98s=stis_spec.wavelength
flux_98s=stis_spec.flux
err_98s=stis_spec.error

readcol,'sn1995n/sn1995N-19970206.000-hst.txt',f='f,f',lam_95n,flux_95n

plotps,'uv_spectra.eps'
device,/portrait,xsize=8.5,ysize=7.4,/inches
!p.font=0
multiplot,/default
blue=getcolor('blue',!D.Table_Size-3)
red=getcolor('red',!D.Table_Size-4)
orange=getcolor('orange',!D.Table_Size-5)
purple=getcolor('purple',!D.Table_Size-6)
green=getcolor('green',!D.Table_Size-7)
grey=getcolor('grey',!D.Table_Size-8)
yellow=getcolor('Dodger Blue',!D.Table_Size-9)
forest=getcolor('Forest Green',!D.Table_Size-10)
brightgreen=getcolor('green',!D.Table_Size-11)
magenta=getcolor('magenta',!D.Table_Size-12)
multiplot,[0,1,5,0,0]

ymin=min(fuv_flux_10jl)
ymax=max(fuv_flux_10jl)
xticks=3
xtickv=[1000,2000,3000,4000]
xtickname=[' ',' ',' ',' ']
plot,fuv_lam_10jl,fuv_flux_10jl,xstyle=1,ystyle=1,xthick=3,ythick=3,charthick=3,charsize=1,xtit=xtit,ytit=ytit,/noerase,/nodata,xrange=[1000,4000],/xlog,/ylog,xticks=xticks,xtickv=xtickv,xtickname=xtickname,yrange=[3.d-17,5.d-16]
;plot,fuv_lam_10jl,fuv_flux_10jl,xstyle=1,ystyle=1,xthick=3,ythick=3,charthick=3,charsize=1,xtit=xtit,ytit=ytit,/noerase,/nodata,xrange=[1000,2000],xticks=xticks,xtickv=xtickv,xtickname=xtickname,yrange=[3.d-17,5.d-16]
dif=80.
c=2.98d18                       ;angstrom/s
vr=dif*c/6562.8
fuv_lam_10jl=fuv_lam_10jl/((vr/c)+1.)
nuv_lam_10jl=nuv_lam_10jl/((vr/c)+1.)
oplot,fuv_lam_10jl,smooth(fuv_flux_10jl,10),thick=4,color=blue
oplot,nuv_lam_10jl,smooth(nuv_flux_10jl,10),thick=4,color=blue

items=['SN 2010jl','SN 2005ip','SN 1998S','SN 1995N']
colors=[blue,red,forest,orange]
;legend,items,color=colors,linestyle=0,thick=4,/right
xyouts,0.17,0.9,'SN 2010jl',color=blue,/normal
plotlines,label=1
multiplot

plot,fuv_lam_05ip,fuv_flux_05ip,xstyle=1,ystyle=1,xthick=3,ythick=3,charthick=3,charsize=1,xtit=xtit,ytit=ytit,/noerase,/nodata,xrange=[1000,4000],/xlog,/ylog,xticks=xticks,xtickv=xtickv,xtickname=xtickname,yrange=[1.d-18,1.d-15]
;plot,fuv_lam_05ip,fuv_flux_05ip,xstyle=1,ystyle=1,xthick=3,ythick=3,charthick=3,charsize=1,xtit=xtit,ytit=ytit,/noerase,/nodata,xrange=[1000,2000],xticks=xticks,xtickv=xtickv,xtickname=xtickname,yrange=[1.d-18,5.d-16]
dif=40.
c=2.98d18                       ;angstrom/s
vr=dif*c/6562.8
fuv_lam_05ip=fuv_lam_05ip/((vr/c)+1.)
nuv_lam_05ip=nuv_lam_05ip/((vr/c)+1.)
oplot,fuv_lam_05ip,smooth(fuv_flux_05ip,10),thick=4,color=red
oplot,nuv_lam_05ip,smooth(nuv_flux_05ip,10),thick=4,color=red
xyouts,0.17,0.7,'SN 2005ip',color=red,/normal
plotlines,label=0
multiplot

plot,lam_98s,flux_98s,xstyle=1,ystyle=1,xthick=3,ythick=3,charthick=3,charsize=1,xtit=xtit,ytit=ytit,/noerase,/nodata,xrange=[1000,4000],/xlog,/ylog,xticks=xticks,xtickv=xtickv,xtickname=xtickname,yrange=[1.d-17,5.d-15]
;plot,lam_98s,flux_98s,xstyle=1,ystyle=1,xthick=3,ythick=3,charthick=3,charsize=1,xtit=xtit,ytit=ytit,/noerase,/nodata,xrange=[1000,2000],xticks=xticks,xtickv=xtickv,xtickname=xtickname,yrange=[1.d-17,5.d-16]
oplot,lam_98s,smooth(flux_98s,10),thick=4,color=forest
xyouts,0.17,0.49,'SN 1998S',color=forest,/normal
plotlines,label=0
multiplot

plot,lam_95n,flux_95n,xstyle=1,ystyle=1,xthick=3,ythick=3,charthick=3,charsize=1,xtit=xtit,ytit=ytit,/noerase,/nodata,xrange=[1000,4000],/xlog,/ylog,xticks=xticks,xtickv=xtickv,xtickname=xtickname,yrange=[1.d-17,5.d-15]
;plot,lam_95n,flux_95n,xstyle=1,ystyle=1,xthick=3,ythick=3,charthick=3,charsize=1,xtit=xtit,ytit=ytit,/noerase,/nodata,xrange=[1000,2000],xticks=xticks,xtickv=xtickv,xtickname=xtickname,yrange=[1.d-17,5.d-16]
oplot,lam_95n,smooth(flux_95n,1),thick=4,color=orange
xyouts,0.17,0.29,'SN 1995N',color=orange,/normal
plotlines,label=0
multiplot

xticks=3
xtickv=[1000,2000,3000,4000]
xtickname=['1000','2000','3000','4000']
plot,fuv_lam_09ip,fuv_flux_09ip,xstyle=1,ystyle=1,xthick=3,ythick=3,charthick=3,charsize=1,xtit=xtit,ytit=ytit,/noerase,/nodata,xrange=[1000,4000],/xlog,/ylog,xticks=xticks,xtickv=xtickv,xtickname=xtickname,yrange=[1.d-18,1.d-15]
;plot,fuv_lam_09ip,fuv_flux_09ip,xstyle=1,ystyle=1,xthick=3,ythick=3,charthick=3,charsize=1,xtit=xtit,ytit=ytit,/noerase,/nodata,xrange=[1000,2000],xticks=xticks,xtickv=xtickv,xtickname=xtickname,yrange=[1.d-19,5.d-17]
dif=-50.
c=2.98d18                       ;angstrom/s
vr=dif*c/6562.8
fuv_lam_09ip=fuv_lam_09ip/((vr/c)+1.)
;nuv_lam_09ip=nuv_lam_09ip/((vr/c)+1.)
oplot,fuv_lam_09ip,smooth(fuv_flux_09ip,15),thick=4,color=magenta
;oplot,nuv_lam_09ip,smooth(nuv_flux_09ip,10),thick=4,color=magenta
xyouts,0.17,0.2,'SN 2009ip',color=magenta,/normal
plotlines,label=0

device,/close
set_plot,'x'
stop

END
