; ============================================
;       Autenticação de Carregador EV
; ============================================

section .data
    msg_modelo      db "Digite o modelo do carro: ", 0
    msg_conectado   db "Veiculo conectado? (S/N): ", 0
    msg_bateria     db "Nivel da bateria (0-100): ", 0
    msg_ok          db "Autenticacao OK! Carregamento iniciado.", 10, 0
    msg_desconect   db "Erro: Veiculo nao conectado.", 10, 0
    msg_cheia       db "Bateria ja esta cheia!", 10, 0
    msg_invalido    db "Entrada invalida.", 10, 0

section .bss
    modelo          resb 32     
    resposta        resb 2      
    bateria_buf     resb 4      

section .text
    global _start

; 
%macro print 2
    mov eax, 4          ; syscall sys_write (em 32 bits é 4)
    mov ebx, 1          
    mov ecx, %1         ; endereço da string
    mov edx, %2         
    int 0x80            
%endmacro

_start:
    ; Pede modelo do carro
    print msg_modelo, 26
    mov eax, 3          ; sys_read (em 32 bits é 3)
    mov ebx, 0          ; std
    mov ecx, modelo
    mov edx, 32
    int 0x80

    ; Pede nivel da bateria
    print msg_bateria, 26
    mov eax, 3
    mov ebx, 0
    mov ecx, bateria_buf
    mov edx, 4
    int 0x80

    ; Converte ASCII para numero (usando registradores de 32 bits)
    movzx eax, byte [bateria_buf]
    sub eax, '0'        
    imul eax, 10
    movzx ebx, byte [bateria_buf + 1]
    sub ebx, '0'
    add eax, ebx        ; eax = valor numerico

    cmp eax, 100
    jge bateria_cheia

    ; Pede status de conexão
    print msg_conectado, 26
    mov eax, 3
    mov ebx, 0
    mov ecx, resposta
    mov edx, 2
    int 0x80

    movzx eax, byte [resposta]
    cmp eax, 'S'
    je conectado
    cmp eax, 'N'
    je desconectado

    print msg_invalido, 18
    jmp sair

conectado:
    print msg_ok, 40
    jmp sair

desconectado:
    print msg_desconect, 29
    jmp sair

bateria_cheia:
    print msg_cheia, 22

sair:
    mov eax, 1          ; sys_exit (em 32 bits é 1)
    xor ebx, ebx        
    int 0x80