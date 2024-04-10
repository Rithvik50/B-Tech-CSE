#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/fs.h>
#include <linux/uaccess.h>
#include <linux/string.h>
#include <linux/sched.h>
#include <linux/kthread.h>

#define MAX_USERS 100

struct User {
    char username[50];
    int score;
    char platform[20];
};

static struct User users[MAX_USERS];
static int numUsers = 0;

static int addUser(const char *username, int score, const char *platform) {
    if (numUsers >= MAX_USERS) {
        printk(KERN_ERR "User limit exceeded\n");
        return -ENOMEM;
    }

    strncpy(users[numUsers].username, username, sizeof(users[numUsers].username) - 1);
    users[numUsers].username[sizeof(users[numUsers].username) - 1] = '\0'; // Ensure null-terminated string
    users[numUsers].score = score;
    strncpy(users[numUsers].platform, platform, sizeof(users[numUsers].platform) - 1);
    users[numUsers].platform[sizeof(users[numUsers].platform) - 1] = '\0'; // Ensure null-terminated string

    numUsers++;
    return 0;
}

static void listUsers(void) {
    int i;
    printk(KERN_INFO "List of Users:\n");
    for (i = 0; i < numUsers; i++) {
        printk(KERN_INFO "Username: %s\n", users[i].username);
        printk(KERN_INFO "Score: %d\n", users[i].score);
        printk(KERN_INFO "Platform: %s\n\n", users[i].platform);
    }
}

static int mykernel_thread(void *data) {
    // Add users in the kernel thread
    addUser("Destiny13CR", 1000, "PC");
    addUser("EndtailFox", 1500, "PS5");
    addUser("M01stCr1t1k4l", 2500, "Xbox One");

    // List users in the kernel thread
    listUsers();

    return 0;
}

static int __init mykernel_init(void) {
    struct task_struct *task;

    printk(KERN_INFO "Parent process (PID: %d) started\n", current->pid);

    // Create a kernel thread
    task = kthread_run(mykernel_thread, NULL, "mykernel_thread");
    if (IS_ERR(task)) {
        printk(KERN_ERR "Failed to create kernel thread\n");
        return PTR_ERR(task);
    }

    return 0;
}

static void __exit mykernel_exit(void) {
    printk(KERN_INFO "Exiting kernel module\n");
}

module_init(mykernel_init);
module_exit(mykernel_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Rithvik Muthyalapati");
MODULE_DESCRIPTION("Managing video game users using a kernel");

/*
1) make
2) sudo insmod gameserver.ko
3) sudo dmesg
4) sudo rmmod gameserver.ko
5) sudo dmesg -c
*/