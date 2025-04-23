llvm = r'''@s1 = constant [4 x i8] c"Hi Rithvik Muthyalapati Section H PES2UG22CS451\0a\00"

define i32 @main() {
    %s1_ptr = getelementptr [4 x i8], [4 x i8]* @s1, i32 0, i32 0

    call i32(i8*, ...) @printf(i8* %s1_ptr)
    
    ret i32 0
}'''

with open('output.ll', 'w') as file:
    file.write(llvm)