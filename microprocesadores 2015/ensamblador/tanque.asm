page 60h,132h
title pixel
.model small
.stack 64h
.data   

    
    ciclo  db '50','$'  ;esta se la va a utilizar para hacer 20 pixeles seguidos
    cambio db 0  
    ganaste db 'GANASTE !!!!  :3 ','$' 
    perdiste db 'PERDISTE !!!! :( ','$'
    
    
    
    
.code
    inicio proc far
        mov ax,@data ;lleva los datos
        mov ds,ax    ;a su registro
        mov es,ax   
        
       
        
        
        call modogra
        call dibujarTanque
        call dibujarObjetivo      
        mov dx,10
          
        cicloabajo:
        
            mov cx,100
            call moverobjetivoabajo
            inc dx
             
            
                mov ah,01h
                int 16h
                jne ciclodisparo
             
            cmp dx,180  
            je cicloarriba
            jmp cicloabajo 
            
        cicloarriba:
        
            mov cx,100
            call moverobjetivoarriba
            dec dx  
            
            
                mov ah,01h
                int 16h
                jne ciclodisparo
            
            
            
            cmp dx,10
            je cicloabajo
            jmp cicloarriba 
            
            
        ciclodisparo:
            call disparar 
            
        
        
        comparacion1:    
        cmp bh,95
        ja comparacion2
        jmp perdisteciclo
            
            comparacion2:
                cmp bh,107
                jb ganasteciclo
                jmp perdisteciclo
            
            
        ganasteciclo: 
            call modotext
            call limpiar
            call cursor
            
            mov ax,0000h
            mov ah,09h
            lea dx,ganaste
            int 21h
            call pausa
            jmp salir
            
       perdisteciclo:
            call modotext
            call limpiar
            call cursor
            
            mov ax,0000h
            mov ah,09h
            lea dx,perdiste
            int 21h
            call pausa
            jmp salir  
            
        
       salir:
        mov ax,4c00h
        int 21h       
                       
            
    inicio endp
    
    limpiar proc near  
        mov ah,00h ;limpia la pantalla
		mov al,03h
		int 10h
        ret
    limpiar endp
    
    cursor proc near
        mov ah,02h
        mov dx,0505h
        int 10h
        ret
    cursor endp 
    
    disparar proc near
        
         mov bh,dl
         mov cx,35
         mov dx,106
         mov al,28h
         mov ah,0ch
         mov bl,0
        
        disparomov1:
                int 10h
                inc cx 
                inc bl
                cmp bl,3
                ja corte
                continuaciondisparo:      
                cmp bl,250
                jne disparomov1
                
         jmp comparacion1
                
         corte:
            dec cx
            dec cx
            mov al,00h
            int 10h
            mov al,28h
            inc cx
            inc cx 
            jmp continuaciondisparo
            
         
        
         ret
        
        
    disparar endp
    
    moverobjetivoabajo proc near
         
        mov al,0h
        mov ah,0ch
        mov bl,0
        
        objetivomov1:
                int 10h
                inc cx 
                inc bl
                cmp bl,3
                jne objetivomov1 
                
        add dx,10 
        mov cx,100
        
        mov al,78h
        mov bl,0  
        
        
        objetivomov2:
                int 10h
                inc cx 
                inc bl
                cmp bl,3
                jne objetivomov2 
                
        sub dx,10
        
        ret  
        
    moverObjetivoabajo endp   
    
    moverobjetivoarriba proc near
         
        mov al,78h
        mov ah,0ch
        mov bl,0
        
        objetivomov3:
                int 10h
                inc cx 
                inc bl
                cmp bl,3
                jne objetivomov3 
                
        add dx,10 
        mov cx,100
        
        mov al,0h
        mov bl,0  
        
        
        objetivomov4:
                int 10h
                inc cx 
                inc bl
                cmp bl,3
                jne objetivomov4 
                
        sub dx,10
        
        ret  
        
    moverObjetivoarriba endp
    
        
    modogra proc near   ;en esta funcion ponemos al programa en modo grafico
        mov ah,0h
        mov al,13h
        int 10h
        ret
    modogra endp 
    
    moverObjetivo proc near
      
        
    moverObjetivo endp
    
    dibujarObjetivo proc near
        mov al,78h 
        mov cx,100
        mov dx,10
        mov ah,0ch
        
        mov bl,0 
        mov bh,0
        objetivo1:
            objetivo2:
                int 10h
                inc cx 
                inc bl
                cmp bl,3
                jne objetivo2
            mov bl,0
            mov cx,100
            inc dx
            inc bh 
            cmp bh,10 
            jne objetivo1
            
        ret
                          
    dibujarObjetivo endp                      
    
    dibujarTanque proc near 
        mov al,28h 
        mov cx,10
        mov dx,100
        mov ah,0ch
        
        mov bl,0 
        mov bh,0
        tanque1:
            tanque2:
                int 10h
                inc cx 
                inc bl
                cmp bl,15
                jne tanque2
            mov bl,0
            mov cx,10
            inc dx
            inc bh 
            cmp bh,15 
            jne tanque1 
            
            
        mov al,09h 
        mov cx,20 
        mov dx,105
        mov ah,0ch
        mov bl,0 
        mov bh,0
        
        canon1:
            canon2:
                int 10h
                inc cx 
                inc bl 
                cmp bl,15
                jne canon2
            mov bl,0
            mov cx,20
            inc dx
            inc bh 
            cmp bh,4 
            jne canon1
            
                       
                       
        ret
         
        
    dibujarTanque endp
        
        
    linea proc near    ;funcion linea que nos dibuja una linea en pantalla
        
        mov al,28h     ;mueve a "al" el color que tendra la linea en este caso rojo
        
        mov cx,10h     ;empezamos desde el punto 10(hexadecimal) en X
        mov dx,20h     ;empezamos desde el punto 20(hexadecimal) en Y
        mov ah,0ch     ;funcion de dibujado de pixel
        
        mov bl,00h     ;el registro bl lo usamos para nuestro ciclo 
        lea di,ciclo   ;metemos la variable ciclo en el registro destino
            
        lineal:  
        
        inc dx         ;incrementamos posicion en Y
        inc cx         ;incrementamos posicion en X                           
        int 10h        ;interrupcion que dibuja pixel 
        inc bl         ;incrementamos el registro bl
        cmp bl,[di]    ;comparamos si el registro bl es igual al registro destino "osea si el numero de pixeles es igual a 20"
        jne lineal      ;si no es asi repetimos el proceso desde la parte linea en el programa
        
        ret 
    linea endp
        
    pausa proc near   ;funcion pausa que nos pausa el programa
        mov ah,00h
        int 16h
        ret
    pausa endp
    
    modotext proc near
        
        mov ah,13h
        mov al,07h
        int 10h
        ret  
        
    modotext endp
        




end