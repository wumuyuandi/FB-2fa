# FB-2FA

Windows 桌面版 **2FA（TOTP）验证码生成器**，带图形界面，可一键复制验证码。

## 功能

- 输入 Base32 格式的 **2FA Secret**（支持带空格，如 `BK5V TVQ7 D2RB`）
- 点击 **Submit** 生成当前 6 位 TOTP 验证码
- 点击 **Copy** 复制验证码到剪贴板
- 支持打包为独立 `.exe`，无需安装 Python 即可运行

## 环境要求

- Windows 10 / 11
- Python 3.8+（仅源码运行或自行打包时需要）

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行程序

```bash
python 2fa.py
```

### 3. 打包为 exe

双击运行 `build_2fa_exe.bat`，或在命令行执行：

```bash
build_2fa_exe.bat
```

打包完成后，可执行文件位于：

```
dist\2FA验证码生成器.exe
```

可将该 exe 复制到任意 Windows 电脑直接使用。

## 使用说明

1. 在上方 **2FA Secret** 输入框粘贴你的密钥（来自身份验证器 App 或网站提供的 Secret）
2. 点击 **Submit** 生成验证码
3. 验证码每 30 秒刷新一次，过期后重新点击 **Submit** 即可
4. 点击 **Copy** 将验证码复制到剪贴板

> **注意：** Secret 是敏感信息，请勿泄露给他人。本程序仅在本地计算验证码，不会上传任何数据。

## 技术栈

| 组件 | 用途 |
|------|------|
| [pyotp](https://github.com/pyauth/pyotp) | TOTP 算法实现 |
| tkinter | GUI 界面（Python 内置） |
| PyInstaller | 打包为 Windows exe |

## 项目结构

```
FB-2fa/
├── 2fa.py              # 主程序
├── build_2fa_exe.bat   # 一键打包脚本
├── requirements.txt    # Python 依赖
└── README.md           # 说明文档
```

## License

MIT
