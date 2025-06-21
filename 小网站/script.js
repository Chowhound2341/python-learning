// 47游乐园门票系统 JavaScript
class TicketSystem {
    constructor() {
        this.ticketPrices = {
            'INFANT': 0,      // 婴幼儿
            'CHILD': 0,       // 儿童
            'STUDENT': 30,    // 学生
            'ADULT': 68,      // 成人
            'SENIOR': 34,     // 老人
            'DISABLED': 0     // 残疾人
        };
        
        this.ticketTypeNames = {
            'INFANT': '婴幼儿',
            'CHILD': '儿童',
            'STUDENT': '学生',
            'ADULT': '成人',
            'SENIOR': '老人',
            'DISABLED': '残疾人'
        };
        
        this.visitHistory = [];
        this.dailyStats = {
            totalVisitors: 0,
            totalRevenue: 0
        };
        
        this.init();
    }
    
    init() {
        this.updateDateTime();
        this.setupEventListeners();
        this.updateStats();
        
        // 每分钟更新时间
        setInterval(() => {
            this.updateDateTime();
        }, 60000);
    }
    
    updateDateTime() {
        const now = new Date();
        const dateTimeElement = document.getElementById('current-date-time');
        const weatherElement = document.getElementById('weather-status');
        
        const options = {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            weekday: 'long',
            hour: '2-digit',
            minute: '2-digit'
        };
        
        const dateTimeString = now.toLocaleDateString('zh-CN', options);
        dateTimeElement.textContent = dateTimeString;
        
        // 根据时间显示天气状态
        const hour = now.getHours();
        const weatherEmoji = hour < 18 ? '☀️' : '🌙';
        weatherElement.textContent = weatherEmoji;
    }
    
    setupEventListeners() {
        const form = document.getElementById('ticket-purchase-form');
        const newTicketBtn = document.getElementById('new-ticket-btn');
        
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleTicketPurchase();
        });
        
        newTicketBtn.addEventListener('click', () => {
            this.resetForm();
        });
    }
    
    handleTicketPurchase() {
        const age = parseInt(document.getElementById('age').value);
        const isStudent = document.getElementById('is-student').checked;
        const isDisabled = document.getElementById('is-disabled').checked;
        
        if (!this.validateAge(age)) {
            return;
        }
        
        const ticketInfo = this.generateTicket(age, isStudent, isDisabled);
        this.displayTicket(ticketInfo);
        this.saveVisitRecord(ticketInfo);
        this.updateStats();
        
        // 平滑滚动到门票显示区域
        document.getElementById('ticket-display').scrollIntoView({
            behavior: 'smooth'
        });
    }
    
    validateAge(age) {
        if (isNaN(age) || age < 0) {
            alert('❌ 请输入有效的年龄！');
            return false;
        }
        
        if (age > 150) {
            return confirm('⚠️ 年龄输入过大，请确认是否正确？');
        }
        
        return true;
    }
    
    determineTicketType(age, isStudent, isDisabled) {
        if (isDisabled) {
            return 'DISABLED';
        } else if (age < 3) {
            return 'INFANT';
        } else if (age < 18) {
            return 'CHILD';
        } else if (age < 25 && isStudent) {
            return 'STUDENT';
        } else if (age < 60) {
            return 'ADULT';
        } else {
            return 'SENIOR';
        }
    }
    
    applySpecialDiscounts(ticketInfo) {
        const now = new Date();
        const weekday = now.getDay(); // 0是周日，1-6是周一到周六
        const hour = now.getHours();
        
        let discount = 0;
        const specialNotes = [];
        
        // 工作日折扣（周一到周四）
        if (weekday >= 1 && weekday <= 4 && ticketInfo.ticketType === 'ADULT') {
            discount += 0.1;
            specialNotes.push('工作日优惠：9折');
        }
        
        // 早鸟优惠（上午10点前）
        if (hour < 10 && ticketInfo.basePrice > 0) {
            discount += 0.05;
            specialNotes.push('早鸟优惠：额外5%折扣');
        }
        
        // 节假日涨价（周六日）
        if (weekday === 0 || weekday === 6) {
            if (ticketInfo.ticketType === 'ADULT' || ticketInfo.ticketType === 'STUDENT') {
                ticketInfo.basePrice *= 1.2;
                specialNotes.push('周末票价：+20%');
            }
        }
        
        ticketInfo.discount = discount;
        ticketInfo.specialNotes = specialNotes;
        ticketInfo.finalPrice = ticketInfo.basePrice * (1 - discount);
        
        return ticketInfo;
    }
    
    generateTicket(age, isStudent, isDisabled) {
        const ticketType = this.determineTicketType(age, isStudent, isDisabled);
        const basePrice = this.ticketPrices[ticketType];
        
        let ticketInfo = {
            age: age,
            ticketType: ticketType,
            basePrice: basePrice,
            discount: 0,
            finalPrice: basePrice,
            specialNotes: []
        };
        
        // 应用特殊折扣
        ticketInfo = this.applySpecialDiscounts(ticketInfo);
        
        return ticketInfo;
    }
    
    displayTicket(ticketInfo) {
        const ticketDisplay = document.getElementById('ticket-display');
        const now = new Date();
        
        // 生成票号
        const ticketId = `47-${now.getFullYear()}${(now.getMonth()+1).toString().padStart(2,'0')}${now.getDate().toString().padStart(2,'0')}-${(this.visitHistory.length + 1).toString().padStart(4, '0')}`;
        
        // 填充门票信息
        document.getElementById('ticket-id').textContent = ticketId;
        document.getElementById('ticket-age').textContent = `${ticketInfo.age}岁`;
        document.getElementById('ticket-type').textContent = this.ticketTypeNames[ticketInfo.ticketType];
        document.getElementById('ticket-date').textContent = now.toLocaleString('zh-CN');
        
        // 价格信息
        if (ticketInfo.basePrice === 0) {
            document.getElementById('ticket-price').textContent = '🆓 免费入园';
            document.getElementById('discount-info').style.display = 'none';
        } else {
            if (ticketInfo.discount > 0) {
                document.getElementById('original-price').textContent = `¥${Math.round(ticketInfo.basePrice)}`;
                document.getElementById('discount-percent').textContent = `${Math.round(ticketInfo.discount * 100)}%`;
                document.getElementById('final-price').textContent = `¥${Math.round(ticketInfo.finalPrice)}`;
                document.getElementById('ticket-price').textContent = `¥${Math.round(ticketInfo.finalPrice)}`;
                document.getElementById('discount-info').style.display = 'block';
            } else {
                document.getElementById('ticket-price').textContent = `¥${Math.round(ticketInfo.finalPrice)}`;
                document.getElementById('discount-info').style.display = 'none';
            }
        }
        
        // 特殊说明
        if (ticketInfo.specialNotes && ticketInfo.specialNotes.length > 0) {
            const notesList = document.getElementById('notes-list');
            notesList.innerHTML = '';
            ticketInfo.specialNotes.forEach(note => {
                const li = document.createElement('li');
                li.textContent = note;
                notesList.appendChild(li);
            });
            document.getElementById('special-notes').style.display = 'block';
        } else {
            document.getElementById('special-notes').style.display = 'none';
        }
        
        // 生成二维码艺术
        this.generateQRCode();
        
        // 显示门票并添加动画
        ticketDisplay.style.display = 'block';
        ticketDisplay.classList.add('bounce-in');
        
        // 隐藏表单
        document.querySelector('.ticket-form').style.display = 'none';
    }
    
    generateQRCode() {
        const qrArt = [
            "██████████████    ██  ██████████████",
            "██          ██  ████  ██          ██",
            "██  ██████  ██    ██  ██  ██████  ██",
            "██  ██████  ██  ██    ██  ██████  ██",
            "██  ██████  ██    ██  ██  ██████  ██",
            "██          ██  ████  ██          ██",
            "██████████████  ██  ██████████████",
            "                ██                  ",
            "██  ██    ██████    ██    ██  ████  ",
            "    ██████    ██  ████████  ██    ██",
            "██    ██  ██████    ██  ██    ██████",
            "██████████████  ██    ██████    ██  ",
            "██          ██    ██    ██  ████    ",
            "██  ██████  ██  ██████████    ██████",
            "██  ██████  ██      ██    ██████  ██",
            "██  ██████  ██  ██  ██████    ██    ",
            "██          ██    ████  ██████  ████",
            "██████████████    ██    ██  ██    ██"
        ];
        
        document.getElementById('qr-code').textContent = qrArt.join('\n');
    }
    
    saveVisitRecord(ticketInfo) {
        const visitRecord = {
            timestamp: new Date().toISOString(),
            age: ticketInfo.age,
            ticketType: ticketInfo.ticketType,
            price: ticketInfo.finalPrice,
            discounts: ticketInfo.specialNotes
        };
        
        this.visitHistory.push(visitRecord);
        this.dailyStats.totalVisitors += 1;
        this.dailyStats.totalRevenue += ticketInfo.finalPrice;
    }
    
    updateStats() {
        document.getElementById('total-visitors').textContent = this.dailyStats.totalVisitors;
        document.getElementById('total-revenue').textContent = `¥${Math.round(this.dailyStats.totalRevenue)}`;
        
        if (this.dailyStats.totalVisitors > 0) {
            const avgPrice = this.dailyStats.totalRevenue / this.dailyStats.totalVisitors;
            document.getElementById('avg-price').textContent = `¥${Math.round(avgPrice)}`;
        } else {
            document.getElementById('avg-price').textContent = '¥0';
        }
    }
    
    resetForm() {
        // 显示表单
        document.querySelector('.ticket-form').style.display = 'block';
        
        // 隐藏门票显示
        document.getElementById('ticket-display').style.display = 'none';
        
        // 重置表单
        document.getElementById('ticket-purchase-form').reset();
        
        // 滚动到表单
        document.querySelector('.ticket-form').scrollIntoView({
            behavior: 'smooth'
        });
    }
}

// 页面加载完成后初始化系统
document.addEventListener('DOMContentLoaded', () => {
    // 添加加载动画
    document.body.classList.add('fade-in');
    
    // 初始化门票系统
    const ticketSystem = new TicketSystem();
    
    // 添加一些交互效果
    addInteractiveEffects();
});

function addInteractiveEffects() {
    // 为所有按钮添加点击效果
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
    
    // 为表单输入添加焦点效果
    const inputs = document.querySelectorAll('input');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        
        input.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
        });
    });
    
    // 添加鼠标跟随效果
    document.addEventListener('mousemove', (e) => {
        const cursor = document.querySelector('.cursor');
        if (!cursor) {
            const newCursor = document.createElement('div');
            newCursor.className = 'cursor';
            document.body.appendChild(newCursor);
        }
    });
}

// 添加自定义CSS动画样式
const style = document.createElement('style');
style.textContent = `
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.6);
        transform: scale(0);
        animation: ripple-animation 0.6s linear;
        pointer-events: none;
    }
    
    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
    
    .focused {
        transform: translateY(-2px);
        transition: transform 0.3s ease;
    }
    
    .cursor {
        width: 20px;
        height: 20px;
        border: 2px solid #667eea;
        border-radius: 50%;
        position: fixed;
        pointer-events: none;
        z-index: 9999;
        transform: translate(-50%, -50%);
        transition: transform 0.1s ease;
    }
`;
document.head.appendChild(style);
