@s1 = constant [49 x i8] c"Hi Rithvik Muthyalapati Section H PES2UG22CS451\0a\00"
declare i32 @printf(i8*, ...)
define i32 @main() {
    %s1_ptr = getelementptr [49 x i8], [49 x i8]* @s1, i32 0, i32 0

    call i32(i8*, ...) @printf(i8* %s1_ptr)

    ret i32 0
}