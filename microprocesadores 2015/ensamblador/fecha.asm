page 60,132
    title mes.exe
   .model
   .stack
   .data
   
 grabdia DB ?
 grabmes DB ?
 grabano DW ?
 dia     DB 10
 mes     DB 13
 sem     DB 12
 ano     DB 4 DUP(' '),'$'
 tabla1  DB 'DOMINGO  $  ','LUNES  $    '
         DB 'MARTES  $   ','MIERCOLES  $'
         DB 'JUEVES  $   ','VIERNES  $  '
         DB 'SABADO  $   '          
 tabla2  DB 'ENERO  $     ','FEBRERO  $   ','MARZO  $     '
         DB 'ABRIL  $     ','MAYO  $      ','JUNIO  $     '
         DB 'JULIO  $     ','AGOSTO  $    ','SEPTIEMBRE  $'
         DB 'OCTUBRE$     ','NOVIEMBRE  $ ','DICIEMBRE   $'
 
       .CODE
INICIO PROC       FAR
       MOV        AX,@DATA
         MOV        DS,AX
         MOV        ES,AX
         MOV        AX,0600H
         CALL       limpiar 
         CALL       cursor
         MOV        AH,2AH;para obtener fecha
         INT        21H    ; del sistema
         MOV        grabmes,DH ;mes
         MOV        grabdia,DL ;dia del mes
         MOV        grabano,CX ;ANO
         CALL       mostrar_sem  ;dia de la semana 
         CALL       mostrar_mes
         CALL       mostrar_dia
         CALL       mostrar_ano
         CALL       teclado
         CALL       limpiar
         MOV        AX,4C00H
         INT        21H
INICIO ENDP
mostrar_sem PROC    NEAR
            MUL     sem
            LEA     DX,tabla1
            ADD     DX,AX
            MOV     AH,09H
            INT     21H
            RET
mostrar_sem ENDP
mostrar_mes PROC    NEAR
            MOV     AL,grabmes
            DEC     AL
            MUL     mes
            LEA     DX,tabla2
            ADD     DX,AX
            MOV     AH,09
            INT     21H
            RET
mostrar_mes ENDP

mostrar_dia PROC    NEAR
            ;MOVZX   AX,grabdia
            DIV     dia
            OR      AX,3030H
            MOV     BX,AX
            
            MOV     AH,02H
            MOV     DL,BL
            INT     21H
            
            MOV     AH,02H
            MOV     DL,BH
            INT     21H
            RET
mostrar_dia ENDP
mostrar_ano PROC    NEAR
            MOV     AX,grabano ;esta en exadecimal
            lea     si,ano+3
            mov     cx,10
A10:        
            cmp     ax,cx
            jb      A20
            xor     dx,dx ;eldx se hace cero 
            DIV     cx ;div a ax y dx, ax;cociente, dx:residuo                        
            OR      dl,30H ;colorear el 3 para ascii
            MOV     [si],dl
            dec     si
            jmp     A10
A20:         
            or      al,30h
            mov     [si],al
            
            mov     ah,02h
            MOV     BH,00
            MOV     DH,11 
            MOV     DL,47
            int     10h
            
            mov     ah,09h
            lea     dx,ano
            int     21h
            
            RET
mostrar_ano ENDP
teclado     PROC    NEAR
            MOV     AH,0
            INT     16H  
            RET
teclado     ENDP
limpiar     PROC    NEAR
            MOV     AX,0600H 
            MOV     BH,17H
            MOV     CX,0000
            MOV     DX,184FH
            INT     10H
            RET
limpiar     ENDP    
cursor      PROC    NEAR
            MOV     AH,02H
            MOV     BH,00
            MOV     DH,11
            MOV     DL,28   
            INT     10H
            RET
cursor      ENDP
            END     INICIO
