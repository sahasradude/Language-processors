read n
load zero
back: read x
load sum
add x
store sum
load n
sub one
jz done
store n
jmp back
done: write sum
stop
endp
n db ?
x db ?
zero const 0
one const 1
sum db 0
end
