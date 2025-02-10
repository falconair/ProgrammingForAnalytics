
# **Introduction to the Linux Command Line**

Your computer has a file system, organized in a heirarchy.

### Windows file system looks something like this:

```
c:\
    ...
    Program Files
    Program Files (x86)
    Windows
    Users
        Public
        shahbaz
            Desktop
            Documents
            Pictures
            .gitconfig
            ...
```

### Mac users' file system looks something like this

```
/
    ...
    tmp/
    Applications/
    Library/
    Users/
        shahbaz/
            Applications/
            Desktop/
            Downloads/
            ...
```

### Linux users' file system looks something like this

```
/
    ...
    tmp/
    bin/
    opt/
    home/
        shahbaz/
```


## **Week 1: Exploring the Command Line**
### **1. Connecting to a Remote Machine**
- Check network connectivity with `ping`:
  ```bash
  ping google.com
  ```

- Use `ssh` to log in:
  ```bash
  ssh -l <username> <remote_ip_address>
  ```
  - **Example:** `ssh -l student 192.168.1.10`

### **2. Basic Navigation**

A path tells your a location in a file system: `/home/shahbaz/myfile.txt` tells you that you can access the file `myfile.txt` by navigating to the "top" `/`, then changing directory to `home`, then to `shahbaz`.

Notice that there is similar to a web url: `https://datascience.uchicago.edu/education/masters-programs/ms-in-applied-data-science/`



- **Commands**:
  - `pwd` – Print working directory.
  - `ls` – List files and directories.
  - `cd` – Change directory.
  - `tree` – Show directory structure (if installed).
- Explore:
  - Use `ls -a` to see hidden files (`.bashrc`, `.profile`).
  - Understand paths:
    - `.` – Current directory
    - `..` – Parent directory
    - `~` – Home directory
  - Absolute vs. Relative paths.

### **3. Viewing File Contents**
- **Commands**:
  - `head <file>` – View the first few lines.
  - `cat <file>` – Show entire file (be cautious with large files).
  - `less <file>` – Paginated view with navigation.

### **Exercise**
- Navigate to `/opt/mleng_class/datasets/names`
- What files do you see in that directory?
- Take a look at the first few male and female names
- Count the number of lines in `male.txt` and `female.txt` files (hint, use `wc -l`)

### **4. Getting Help**
- **Options**:
  - `--help` or `-h` with most commands.
  - `man <command>` for the manual page.

### **5. Searching and Filtering**
- **Commands**:
  - `which <command>` – Find command location.
  - `find <path> -name <filename>` – Search for a file called `<filename>` "under" the path `<path>`.
  - `grep <pattern> <file>` – Look for the text (or pattern) `<pattern>` in a file called `<file>`.
    - Use `grep -i` to ignore case.
    - Combine with regex for advanced filtering.
- Combine commands with pipes (`|`): <== A SUPER POWER!
  ```bash
  cat file.txt | grep "pattern" | head
  ```

### **Exercise**
- Navigate to `/opt/mleng_class/datasets/names`
- In the file `male.txt`, find all names which contains "Quin"
- Make sure the list includes 'Joaquin' and "Quincy" (among others)

---

## **Week 2: Moving and Editing Files**
### **1. File Operations**
- **Commands**:
  - `mkdir` – Create directories.
  - `cp` – Copy files.
  - `mv` – Move or rename files.
  - `rm` – Remove files or directories (`rm -rf` for directories).
  - `wget`/`curl` – Download files.
  - `tar`/`gzip`/`unzip` – Compress and extract files.

### **2. Editing Files**
- Use `nano` for simple edits:
  - Save: `Ctrl + O`
  - Exit: `Ctrl + X`

### **3. Environment and Configuration**
- View or edit:
  - `.bashrc`, `.profile`
  - Add `export PS1="[\u@\h \W]\$ "` to modify the prompt.
- **Environment Variables**:
  - View with `printenv`.
  - Common examples:
    - `$HOME`, `$PATH`

### **4. Diffing Files**
- Compare files:
  ```bash
  diff file1 file2
  ```

### **5. `find` files**
- Compare files:
  ```bash
  find . | grep file_pattern
  ```

### **6. Automating with Loops**
- Process multiple files:
  ```bash
  for file in *.txt; do echo $file; done
  ```

---

## **Week 3: Managing Processes**
### **1. System Info**
- **Commands**:
  - `uname -a` – OS info.
  - `cat /etc/os-release` – Linux distribution.
  - `free -h` – Memory.
  - `df -h` – Disk space.

### **2. Monitoring Processes**
- **Commands**:
  - `ps` – View processes.
  - `top` or `htop` – Interactive monitoring.

### **3. Managing Processes**
- Start a background process:
  ```bash
  long_running_command &
  ```
- Control processes:
  - `Ctrl+C` – Terminate.
  - `Ctrl+Z` – Suspend.
  - `bg` – Resume in the background.
  - `fg` – Bring back to the foreground.
  - `kill -9 <PID>` – Force kill.

### **4. Redirecting Output**
- Save output to a file:
  ```bash
  command > output.txt
  ```
- Append:
  ```bash
  command >> output.txt
  ```

---

## **Week 4: Advanced Concepts**
### **1. Advanced Navigation**
- `cd -` – Return to the last directory.
- Use `tree` for visualization.

### **2. Job Management**
- `jobs` – View running background jobs.
- Use `nohup` to ensure long-running jobs persist:
  ```bash
  nohup command &
  ```

### **3. Regular Expressions**
- Basics:
  - `^` – Start of a line.
  - `$` – End of a line.
  - `.` – Any character.
  - `*` – Zero or more occurrences.
- Combine with `grep`, `sed`, or `awk`.

---

## **Week 5: Capstone**
### **Scenario**:
1. SSH into the remote machine.
2. Use `find`, `grep`, and `nano` to edit configuration files.
3. Start a long-running job with output redirected to a log file.
4. Monitor resources with `top` or `htop`.
5. Schedule periodic tasks with `crontab`:
   ```bash
   crontab -e
   ```
   Example entry:
   ```bash
   0 3 * * * /path/to/script.sh
   ```

---
With help from ChatGPT (free version).