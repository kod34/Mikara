

<h3 align="center"><b>Mikara</b></h3>



---

<p align="center"> Mikara is a tool that takes into input information gathered about a target and generates a passwordlist specific for that target.
    <br> 
</p>

## 📝 Table of Contents

- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)


## 🏁 Getting Started <a name = "getting_started"></a>


### Prerequisites


```
Python
Linux
```

### Installing


```
git clone https://github.com/kod34/Mikara
cd Mikara
chmod +x install.sh
./install.sh
```

## 🎈 Usage <a name="usage"></a>

```
mikara [-h] -o OUTPUT -t TYPE -s SIZE

options:
  -h, --help            show this help message and exit

required named arguments:
  -o OUTPUT, --output OUTPUT wordlist path
  -t TYPE, --type TYPE  list type (simple, moderate, complex, impossible)
  -s SIZE, --size SIZE  minimum word size

```
### Examples:  

```
mikara -o wordlist.txt -t complex -s 16
```

### 📝 Notes  

- Multiple inputs should be separated by spaces.

## ⛏️ Built Using <a name = "built_using"></a>

- Python

## ✍️ Authors <a name = "authors"></a>

- [@kod34](https://github.com/kod34)

## ⚠️ Disclaimer
The sole purpose of writing this program was research, its misuse is the responsibility of the user only.
