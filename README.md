# finance_manager

---

# 个人财务管理系统

这是一个用 Python 编写的简单个人财务管理系统，旨在帮助用户记录收入、支出，并提供财务报表分析。用户可以注册、登录、记录财务数据、查看账户余额、查看各类财务报表等功能。

## 功能

- **用户注册与登录**：支持用户注册新账户，登录已有账户。
- **记录财务数据**：支持记录收入和支出，用户可以选择类别、金额和备注。
- **查看财务状况**：用户可以查看自己的收入、支出和账户余额。
- **生成财务报表**：自动生成财务报表，并显示收入和支出的可视化图表。

## 项目结构

```
your_project_directory/
├── main.py            # 主程序入口
├── user.py            # 用户管理相关代码
├── finance.py         # 财务记录相关代码
├── report.py          # 报表生成相关代码
├── storage.py         # 数据存储和加载功能
├── utils.py           # 辅助工具函数
├── users.json         # 存储用户数据的文件
├── finance.json       # 存储财务记录的文件
└── README.md          # 项目说明文件
```

## 安装和运行

### 1. 安装 Python

确保已安装 Python 3.x 版本。可以通过以下命令检查是否已安装：

```bash
python --version
```

如果没有安装 Python，请访问 [Python 官方网站](https://www.python.org/downloads/) 下载并安装最新版本。

### 2. 安装依赖库

本项目使用了第三方库 `matplotlib` 来生成财务报表图表。请在项目目录下使用以下命令安装所需的库：

```bash
pip install matplotlib
```

### 3. 配置数据文件

在项目目录中，`users.json` 和 `finance.json` 文件分别用于存储用户信息和财务记录。你可以手动创建这些文件，或者直接使用项目中的示例数据。

示例数据（参考上一条对话中的内容）：

- `users.json`: 存储用户的用户名和密码（SHA256 哈希）。
- `finance.json`: 存储用户的收入和支出记录。

### 4. 运行项目

在命令行中进入项目目录并运行 `main.py`：

```bash
python main.py
```

程序会启动并提示你注册或登录。

### 5. 用户操作

运行程序后，您可以通过命令行界面进行以下操作：

#### 注册新用户

选择“注册”选项并输入用户名和密码来创建新账户。

#### 登录

选择“登录”选项并输入用户名和密码进行登录。

#### 记录收入和支出

登录后，你可以选择“记录收入或支出”选项来记录财务数据。你需要提供以下信息：
- 记录类型（收入或支出）
- 金额
- 财务类别（如：工资、餐饮、娱乐等）
- 日期
- 备注（可选）

#### 查看财务状况

你可以选择“查看财务状况”来查看当前账户的总收入、总支出和账户余额。

#### 生成报表

你可以选择“查看报表”来生成和查看财务图表，显示收入和支出的分布情况。

### 6. 退出

选择“退出”选项以退出程序。

## 示例操作流程

1. 启动程序后，输入 `2` 注册新用户（例如：用户名 `alice`，密码 `password`）。
2. 完成注册后，选择 `1` 登录（使用 `alice` 和密码 `password`）。
3. 登录后，选择 `1` 来记录收入或支出，输入相关信息。
4. 选择 `2` 查看财务状况，查看账户余额和财务详情。
5. 选择 `3` 查看报表，查看收入和支出的图表。
6. 选择 `4` 退出程序。

## 数据存储

### 用户数据 (`users.json`)

`users.json` 用于存储已注册的用户信息，文件内容是一个 JSON 数组，每个用户包含 `username`（用户名）和 `password`（经过 SHA256 哈希处理的密码）。

```json
[
    {
        "username": "alice",
        "password": "5e884898da28047151d0e56f8dc6292773603d0d3f4e586e4f5d9f29b1b5e9e5"
    }
]
```

### 财务记录数据 (`finance.json`)

`finance.json` 用于存储用户的收入和支出记录。每条记录包含 `username`（用户名）、`type`（类型：收入或支出）、`amount`（金额）、`category`（类别）、`date`（日期）和 `notes`（备注）。

```json
[
    {
        "username": "alice",
        "type": "收入",
        "amount": 5000,
        "category": "工资",
        "date": "2025-01-10",
        "notes": "1月工资"
    },
    {
        "username": "alice",
        "type": "支出",
        "amount": 200,
        "category": "餐饮",
        "date": "2025-01-11",
        "notes": "午餐"
    }
]
```

## 生成财务报表

财务报表通过 `matplotlib` 库生成图表。可以根据收支类别生成饼图，帮助用户直观了解收入和支出的分布。

## 注意事项

- 程序目前不支持多用户同时在线，仅支持一个用户在一个时间段内操作。
- 如果数据文件丢失或损坏，程序会在下次启动时重新生成空的 `users.json` 和 `finance.json` 文件。

## 贡献

欢迎对本项目进行贡献，如果有任何问题或建议，可以提交 Issue 或 Pull Request。

## 联系方式

- 联系人：wu
- 电子邮件：Wuyou007991@outlook.com

---
