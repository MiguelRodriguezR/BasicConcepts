
; REALIZADO POR:
; JHONATAN ANDRES HERNANDEZ


PAGE 60,132H
TITLE MOVER
.MODEL SMALL
.STACK 64H
.DATA 

    cadena db '*','$'
    
    error db '  => Tecla no valida', 0Dh,0Ah, '$'
    
    cadena1 db 'MENU MOVER POR TECLADO',0Dh,0Ah
            db    '2. ABAJO',0Dh,0Ah
            db    '4. IZQUIERDA',0Dh,0Ah
            db    '6. DERECHA',0Dh,0Ah
            db    '8. ARRIBA',0Dh,0Ah,'$'
            
    
    fila db 14  ;posicion inicial
    columna db 20

   
    
.code


    inicio proc far
        
        mov ax,@data
        mov ds,ax
        mov es,ax 
        
      ciclo:
        call limpiar
        call cursor1
        call mostrar1
        
        
        call cursor
        call mostrar
    
      
      mov ah,00h   ;lee la pulsacion de la tecla
      int 16h 
      
      cmp     al, 52 
       
         je    left
         
      cmp     al, 54
         
         je    right
          
      cmp     al, 56
        
         je    up 
          
      cmp     al, 50
         
         je    down
           
         
      call mostrar_e  ; muestra error si es diferente la tecla
    
   
       
     ;*** PROCEDIMIENTOS *** 
       
        
      limpiar proc near
      mov ax,0600h
      mov bh,71h
      mov cx, 0000h
      mov dx,184fh 
      int 10h
      ret
      limpiar endp 
      
      cursor1 proc near
        mov ah,02h
        mov bh,00
        mov dx,0110h
        int 10h
        ret
      cursor1 endp     
       
       
        
      cursor proc near
         mov ah,02h
         mov bh,00
         mov dh,fila    ;fila
         mov dl,columna    ;columna
         int 10h  
         ret
      cursor endp
      
      
      left proc near
        call limpiar
         mov ah,02h
         mov bh,00
         mov dh,fila    ;fila en la misma posicion
         dec columna   ; columna -1 posicion en el eje X    
         int 10h
         jmp ciclo  
     left endp 
      
      
     right proc near 
        call limpiar
        mov ah,02h
        mov bh,00
        mov dh,fila    ;fila en la misma posicion
        inc columna    ; columna +1 posicion en el eje X
        int 10h 
        jmp ciclo
     right endp 
      
     up proc near 
        call limpiar
        mov ah,02h
        mov bh,00  
        dec fila          ;fila -1 posicion en el eje Y
        mov dl,columna    ;columna en la misma posicion
        int 10h 
        jmp ciclo
     up endp
              
     down proc near 
        call limpiar
        mov ah,02h
        mov bh,00  
        inc fila         ; fila +1 posicion en el eje Y
        mov dl,columna   ;columna en la misma posicion
        int 10h 
        jmp ciclo
     down endp
              
              
      mostrar proc near
        mov ah,09h
        lea dx,cadena
        int 21h
        ret 
      mostrar endp
      
      
      mostrar_e proc near
         mov ah,09h
         lea dx,error          
         int 21h
         call pausa
         jmp ciclo 
      mostrar_e endp 
      
      mostrar1 proc near
        mov ah,09h
        lea dx,cadena1
        int 21h
        ret
      mostrar1 endp
      
      pausa proc near
        mov ah,00h
        int 16h
        ret
     pausa endp
      
       
      
   mov ax,4c00h
   int 21h 
      
 end 
      
     
     
     