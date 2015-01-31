PRO plot06gy

stis_06gy=mrdfits('2006gy_all_x1dsum.fits',1,h)
lam_06gy=stis_06gy.wavelength
flux_06gy=stis_06gy.flux
err_06gy=stis_06gy.error

plotps,'stis_06gy.eps'
device,/portrait,xsize=8.5,ysize=7.4,/inches
!p.font=0
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

;06gy
;xticks=3
;xtickv=[4000,5000,6000,7000]
;xtickname=['4000','5000','6000','7000']
plot,lam_06gy,flux_06gy,xstyle=1,ystyle=1,xthick=3,ythick=3,charthick=3,charsize=1,xtit=xtit,ytit=ytit,/noerase,/nodata,yrange=[3.d-18,1.d-16],title='STIS SN 2006gy'
oplot,lam_06gy,smooth(flux_06gy,20),thick=4

device,/close
set_plot,'x'
stop
END
