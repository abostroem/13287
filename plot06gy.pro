PRO PLOTLINES,multi

blue=getcolor('blue',!D.Table_Size-4)
gray=getcolor('gray',!D.Table_Size-11)
;overplot lines
IF multi EQ 0 THEN lambda=[3586,4232,4340,4861,5876,6560,6680,7065,7722,6312,7155,7751,8498,8542,8662,4600,5468,5612,4711,5536,5755,7281,6238,6157,7324,4700,7378,6373,6086,4089,6723,3727,8727];,7291];8446,9069]
IF multi EQ 0 THEN lambda=[3586,4232,4340,4861,5876,6560,6680,7065,7722,6312,7155,7751,8498,8542,8662,4600,5468,5612,4711,5536,5755,7281,6238,6157,7324,7378,6373,6086,4089,6723,3727,8727,9020,9230]
IF multi EQ 1 THEN lambda=[4069,4570,7329,7291,5006,5577,6300,7773,5900,7324,8617,8727,9340,9825,10250,10830,11310,12570,12940,13210,13720,15330,15990,16460,18090,6560];from Mazzali et al. 2010, MNRAS, 408, 87
IF multi EQ 1 THEN lambda=[7254,9263,7329,7319,5006,5577,6300,7773,7324,8727,9825,10250,10830,11310,12570,12940,13210,13720,15330,15990,16460,18090];from Mazzali et al. 2010, MNRAS, 408, 87

;alpha=greek('alpha')
IF multi EQ 0 THEN names=['[Fe VII] 3586','[Ni XII] 4232','H!9g!X 4340','H!9b!X 4861','He I 5876','H!9a!X 6560','He I 6680','He I 7065','[S I] 7722','[S II] 6312','[Ar III] + [Fe II]','[Ar III] 7751',' ','Ca II IR','  ','Mg I] 4570','SII 5468','S II 5612,5654','[Ar IV] 4711','[Ar X] 5536','[N II] 5755','He I 7281','Fe II 6238','O I 6157','Ca II] 7324','[Fe III] Blend','Ni II','Fe X','[Fe VII]','Si I','[S II]','[O II]','[C I]'];,'Ca 7291'];'O I 8446','[S III] 9069']
IF multi EQ 0 THEN names=['[Fe VII] 3586','[Ni XII] 4232','H!9g!X 4340','H!9b!X 4861','He I 5876',' ','He I 6680','He I 7065','[S I] 7722','[S II] 6312','[Ar III] + [Fe II]','[Ar III] 7751',' ','Ca II IR','  ','Mg I] 4570','SII 5468','S II 5612,5654','[Ar IV] 4711','[Ar X] 5536','[N II] 5755','He I 7281','Fe II 6238','O I 6157','Ca II] 7324 + [O II] 7325','Ni II','Fe X','[Fe VII]','Si I','[S II]','[O II]','[C I]','Pa!9h!X','Pa!9z!X']
IF multi EQ 1 THEN names=['[S II] 4069, 4076','Mg I] 4570','Ca II] 7324/[O II] 7325','Ca 7291/[O II] 72XX','[O III] 4959,5006','[O I] 5577','[O I] 6300/6364','O I 7773','Na I D',' ','[Fe II] 8617','[C I] 8727','[Co II] 9340, 9345, O I 9264','[C I] 9825, 9850','[Co II] 1.019, 1.025, 1.028','[S I] 1.083','[S I] 1.131','[Fe II] 1.257, 1.279','[Fe II] 1.294','[Fe II] 1.321','[Fe II] 1.372','[Fe II] 1.533','[Fe II] 1.599','[Si I] 1.646,[Fe II] 1.644','[Fe II] 1.809','H!9a!X 6560'];from Mazzali et al. 2010, MNRAS, 408, 87
IF multi EQ 1 THEN names=['[S II] 4069, 4076','Mg I] 4570','[O II] 7325','[O II] 72XX','[O III] 4959,5006','[O I] 5577','[O I] 6300/6364','O I 7773','Na I D',' ','[Fe II] 8617','[C I] 8727','[Co II] 9340, 9345, O I 9264','[C I] 9825, 9850','[Co II] 1.019, 1.025, 1.028','[S I] 1.083','[S I] 1.131','[Fe II] 1.257, 1.279','[Fe II] 1.294','[Fe II] 1.321','[Fe II] 1.372','[Fe II] 1.533','[Fe II] 1.599','[Si I] 1.646,[Fe II] 1.644','[Fe II] 1.809','H!9a!X 6560'];from Mazzali et al. 2010, MNRAS, 408, 87
IF multi EQ 1 THEN names=['O II','O I 9263 blend','[O II] 7319,7329',' ','[O III] 4959,5006','[O I] 5577','[O I] 6300/6364','O I 7773',' ','[C I] 8727','[C I] 9825, 9850','[Co II] 1.019, 1.025, 1.028','[S I] 1.083','[S I] 1.131','[Fe II] 1.257, 1.279','[Fe II] 1.294','[Fe II] 1.321','[Fe II] 1.372','[Fe II] 1.533','[Fe II] 1.599','[Si I] 1.646,[Fe II] 1.644','[Fe II] 1.809'];from Mazzali et al. 2010, MNRAS, 408, 87

constant=0
charsize=0.5
FOR i=0,n_elements(lambda)-1 DO BEGIN
   x=[lambda(i),lambda(i)]
   y=[0,9.d-17]
   IF lambda(i) LT 3000 OR lambda(i) GT 10000 THEN CONTINUE
;   IF lambda(i) LT 4500 OR lambda(i) GT 9000 THEN CONTINUE
   oplot,x,y,thick=2,color=gray,linestyle=2
;   IF i NE 7 AND i NE 4 AND i NE 5 THEN oplot,x,y,thick=4,color=0,linestyle=1
   IF i EQ 9 AND multi EQ 0 THEN xyouts,lambda(i)+20,9.d-17-constant,names(i),orientation=90,charsize=charsize,charthick=3 $
   ELSE IF i EQ 12 THEN xyouts,lambda(i)+20,9.d-17-constant,names(i),orientation=90,charsize=charsize,charthick=3 $ 
   ELSE IF i EQ 0 AND multi EQ 1 THEN xyouts,lambda(i)+25,9.d-17-constant,names(i),orientation=90,charsize=charsize,charthick=3 $
   ELSE IF i EQ 1 AND multi EQ 1 THEN xyouts,lambda(i)-25,9.d-17-constant,names(i),orientation=90,charsize=charsize,charthick=3 $
   ELSE IF i EQ 3 AND multi EQ 1 THEN xyouts,lambda(i)+30,9.d-17-constant,names(i),orientation=90,charsize=charsize,charthick=3 $
   ELSE IF i EQ 4 AND multi EQ 1 THEN xyouts,lambda(i)+50,9.d-17-constant,names(i),orientation=90,charsize=charsize,charthick=3 $
   ELSE IF i EQ 9 AND multi EQ 1 THEN xyouts,lambda(i)+100,9.d-17-constant,names(i),orientation=90,charsize=charsize,charthick=3 $ 
   ELSE IF i EQ 8 AND multi EQ 0 THEN xyouts,lambda(i)-20,9.d-17-constant,names(i),orientation=90,charsize=charsize,charthick=3 $ 
   ELSE IF i EQ 11 AND multi EQ 0 THEN xyouts,lambda(i)+20,9.d-17-constant,names(i),orientation=90,charsize=charsize,charthick=3 $ 
   ELSE IF i EQ 21 AND multi EQ 0 THEN xyouts,lambda(i)-0,9.d-17-constant,names(i),orientation=90,charsize=charsize,charthick=3 $
   ELSE IF i EQ 25 AND multi EQ 0 THEN xyouts,lambda(i)+40,9.d-17-constant,names(i),orientation=90,charsize=charsize,charthick=3 $
   ELSE IF i EQ 26 AND multi EQ 0 THEN xyouts,lambda(i)+40,9.d-17-constant,names(i),orientation=90,charsize=charsize,charthick=3 $
   ELSE IF i EQ 29 AND multi EQ 0 THEN xyouts,lambda(i)+50,9.d-17-constant,names(i),orientation=90,charsize=charsize,charthick=3 $
   ELSE IF i EQ 4 THEN BEGIN
        xyouts,lambda(i)+0,9.d-17-constant,names(i),orientation=90,charsize=charsize,charthick=3 
        oplot,[lambda(i),lambda(i)],[0,9.d-17],thick=2,color=gray,linestyle=2
   ENDIF ELSE BEGIN
      xyouts,lambda(i)+30,9.d-17-constant,names(i),orientation=90,charsize=charsize,charthick=3
      oplot,[lambda(i),lambda(i)],[0,9.d-17],thick=2,color=gray,linestyle=2
     ENDELSE
ENDFOR
;oplot,[6563,6563],[0,16.84],thick=10,color=gray,linestyle=2
IF multi EQ 0 THEN xyouts,6500,9.d-17,'H!9a!X 6560',orientation=90,charsize=charsize,charthick=3
END

PRO plot06gy

stis_06gy=mrdfits('2006gy_all_x1dsum.fits',1,h)
lam_06gy=stis_06gy.wavelength
flux_06gy=stis_06gy.flux
err_06gy=stis_06gy.error

plotps,'stis_06gy.eps'
device,/portrait,xsize=8.5,ysize=4.4,/inches
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

;calculate wavelength shift
vr=5184.*1.d13                  ;angstrom/s
c=3.d18                         ;angstrom/s
;dlam=vr*x/c
;x=x-dlam
lam_06gy=lam_06gy/((vr/c)+1.)
oplot,lam_06gy,smooth(flux_06gy,20),thick=4

plotlines,0
device,/close
set_plot,'x'
stop
END
