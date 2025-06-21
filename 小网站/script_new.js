// 47游乐园门票系统 JavaScript - 终极炫酷版
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
            totalRevenue: 0,
            peakHour: 0,
            currentVisitors: 0
        };
        
        this.currentTheme = this.detectInitialTheme();
        this.isAnimating = false;
        
        this.init();
    }
    
    detectInitialTheme() {
        const now = new Date();
        const hour = now.getHours();
        const month = now.getMonth() + 1;
        const date = now.getDate();
        
        // 节日主题检测
        if ((month === 6 && date === 1) || (month === 10 && date === 1) || 
            (month === 2 && date === 14) || (month === 12 && date === 25)) {
            return 'festival';
        }
        
        // 夜间主题检测
        if (hour >= 19 || hour < 6) {
            return 'night';
        }
        
        return 'day';
    }
    
    init() {
        this.updateDateTime();
        this.setupEventListeners();
        this.updateStats();
        this.initThemeSystem();
        this.initMouseFollower();
        this.initBubbleNotifications();
        this.initAdvancedAnimations();
        
        // 每分钟更新时间
        setInterval(() => {
            this.updateDateTime();
            this.autoThemeSwitch();
        }, 60000);
        
        // 每5秒更新实时数据
        setInterval(() => {
            this.updateRealTimeStats();
        }, 5000);
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
        if (dateTimeElement) {
            dateTimeElement.textContent = dateTimeString;
        }
        
        // 动态天气状态
        const hour = now.getHours();
        let weatherEmoji, weatherText;
        
        if (hour < 6) {
            weatherEmoji = '🌙';
            weatherText = '深夜时光';
        } else if (hour < 10) {
            weatherEmoji = '🌅';
            weatherText = '晨光初照';
        } else if (hour < 14) {
            weatherEmoji = '☀️';
            weatherText = '阳光明媚';
        } else if (hour < 18) {
            weatherEmoji = '🌤️';
            weatherText = '午后时光';
        } else if (hour < 20) {
            weatherEmoji = '🌇';
            weatherText = '夕阳西下';
        } else {
            weatherEmoji = '🌃';
            weatherText = '夜幕降临';
        }
        
        if (weatherElement) {
            weatherElement.innerHTML = `<span class="weather-icon">${weatherEmoji}</span> ${weatherText}`;
        }
    }
    
    setupEventListeners() {
        const form = document.getElementById('ticket-purchase-form');
        const newTicketBtn = document.getElementById('new-ticket-btn');
        
        if (form) {
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                this.handleTicketPurchase();
            });
        }
        
        if (newTicketBtn) {
            newTicketBtn.addEventListener('click', () => {
                this.resetForm();
            });
        }
        
        // 添加键盘快捷键
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'n') {
                e.preventDefault();
                this.resetForm();
            }
            if (e.ctrlKey && e.key === 'd') {
                e.preventDefault();
                this.switchTheme('night');
            }
        });
    }
    
    initThemeSystem() {
        // 创建主题切换按钮组
        const themeToggle = document.createElement('div');
        themeToggle.className = 'theme-toggle';
        
        const dayBtn = this.createThemeButton('day', '☀️', '日间模式');
        const nightBtn = this.createThemeButton('night', '🌙', '夜间模式');
        const festivalBtn = this.createThemeButton('festival', '🎉', '节日模式');
        
        themeToggle.appendChild(dayBtn);
        themeToggle.appendChild(nightBtn);
        themeToggle.appendChild(festivalBtn);
        
        document.body.appendChild(themeToggle);
        
        // 应用初始主题
        this.applyTheme(this.currentTheme);
    }
    
    createThemeButton(theme, icon, title) {
        const btn = document.createElement('button');
        btn.className = `theme-btn ${theme}`;
        btn.innerHTML = icon;
        btn.title = title;
        btn.addEventListener('click', () => this.switchTheme(theme));
        return btn;
    }
    
    switchTheme(newTheme) {
        if (this.currentTheme === newTheme) return;
        
        this.currentTheme = newTheme;
        this.applyTheme(newTheme);
        this.showBubbleNotification(
            this.getThemeIcon(newTheme),
            `已切换到${this.getThemeName(newTheme)}`,
            `享受${this.getThemeName(newTheme)}的视觉体验吧！`
        );
    }
    
    applyTheme(theme) {
        // 清除所有主题类
        document.body.classList.remove('night-theme', 'festival-theme');
        
        // 应用新主题
        if (theme === 'night') {
            document.body.classList.add('night-theme');
        } else if (theme === 'festival') {
            document.body.classList.add('festival-theme');
        }
        
        // 更新主题按钮状态
        document.querySelectorAll('.theme-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        
        const activeBtn = document.querySelector(`.theme-btn.${theme}`);
        if (activeBtn) {
            activeBtn.classList.add('active');
        }
    }
    
    autoThemeSwitch() {
        const newTheme = this.detectInitialTheme();
        if (newTheme !== this.currentTheme && newTheme !== 'day') {
            this.switchTheme(newTheme);
        }
    }
    
    getThemeIcon(theme) {
        const icons = {
            'day': '☀️',
            'night': '🌙',
            'festival': '🎉'
        };
        return icons[theme] || '🎨';
    }
    
    getThemeName(theme) {
        const names = {
            'day': '日间模式',
            'night': '夜间模式',
            'festival': '节日模式'
        };
        return names[theme] || '默认模式';
    }
    
    initMouseFollower() {
        const follower = document.createElement('div');
        follower.className = 'mouse-follower';
        document.body.appendChild(follower);
        
        let mouseX = 0, mouseY = 0;
        let followerX = 0, followerY = 0;
        
        document.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
        });
        
        document.addEventListener('mouseleave', () => {
            follower.style.opacity = '0';
        });
        
        document.addEventListener('mouseenter', () => {
            follower.style.opacity = '1';
        });
        
        // 平滑跟随动画
        const animateFollower = () => {
            const dx = mouseX - followerX;
            const dy = mouseY - followerY;
            
            followerX += dx * 0.1;
            followerY += dy * 0.1;
            
            follower.style.left = followerX + 'px';
            follower.style.top = followerY + 'px';
            
            requestAnimationFrame(animateFollower);
        };
        
        animateFollower();
    }
    
    initBubbleNotifications() {
        // 创建气泡容器
        const bubbleContainer = document.createElement('div');
        bubbleContainer.id = 'bubble-container';
        bubbleContainer.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1080;
        `;
        document.body.appendChild(bubbleContainer);
    }
    
    showBubbleNotification(icon, title, details) {
        const bubble = document.createElement('div');
        bubble.className = 'bubble-notification';
        bubble.innerHTML = `
            <div class="bubble-icon">${icon}</div>
            <div class="bubble-text">${title}</div>
            <div class="bubble-details">${details}</div>
        `;
        
        document.body.appendChild(bubble);
        
        // 显示动画
        setTimeout(() => {
            bubble.classList.add('show');
        }, 100);
        
        // 自动隐藏
        setTimeout(() => {
            bubble.classList.remove('show');
            setTimeout(() => {
                if (bubble.parentNode) {
                    bubble.parentNode.removeChild(bubble);
                }
            }, 300);
        }, 3000);
    }
    
    initAdvancedAnimations() {
        // 为统计数字添加计数动画
        this.animateNumbers();
        
        // 为价格添加闪烁效果（限时优惠）
        this.initPriceAnimations();
        
        // 添加页面加载动画
        this.initPageLoadAnimation();
    }
    
    animateNumbers() {
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                if (mutation.type === 'childList' || mutation.type === 'characterData') {
                    const target = mutation.target.nodeType === Node.TEXT_NODE ? 
                                 mutation.target.parentElement : mutation.target;
                    
                    if (target && target.classList.contains('stat-number')) {
                        this.animateStatNumber(target);
                    }
                }
            });
        });
        
        document.querySelectorAll('.stat-number').forEach(element => {
            observer.observe(element, { 
                childList: true, 
                characterData: true, 
                subtree: true 
            });
        });
    }
    
    animateStatNumber(element) {
        const finalValue = parseInt(element.textContent) || 0;
        const duration = 1000;
        const steps = 30;
        const stepValue = finalValue / steps;
        let currentValue = 0;
        let step = 0;
        
        element.classList.add('updated');
        
        const timer = setInterval(() => {
            currentValue += stepValue;
            step++;
            
            if (step >= steps) {
                currentValue = finalValue;
                clearInterval(timer);
                setTimeout(() => {
                    element.classList.remove('updated');
                }, 500);
            }
            
            if (element.textContent.includes('¥')) {
                element.textContent = `¥${Math.round(currentValue)}`;
            } else {
                element.textContent = Math.round(currentValue).toString();
            }
        }, duration / steps);
    }
    
    initPriceAnimations() {
        const now = new Date();
        const hour = now.getHours();
        
        // 早鸟优惠时段闪烁
        if (hour < 10) {
            document.querySelectorAll('.price-value').forEach(element => {
                element.classList.add('flash');
            });
        }
        
        // 周末特价闪烁
        const weekday = now.getDay();
        if (weekday === 0 || weekday === 6) {
            document.querySelectorAll('.price-item').forEach(element => {
                element.style.animation = 'cardBreath 2s infinite';
            });
        }
    }
    
    initPageLoadAnimation() {
        const sections = document.querySelectorAll('section');
        
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.animation = 'slideInUp 0.6s ease-out forwards';
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);
        
        sections.forEach(section => {
            section.style.opacity = '0';
            section.style.transform = 'translateY(30px)';
            observer.observe(section);
        });
    }
    
    handleTicketPurchase() {
        if (this.isAnimating) return;
        this.isAnimating = true;
        
        const age = parseInt(document.getElementById('age').value);
        const isStudent = document.getElementById('is-student') ? document.getElementById('is-student').checked : false;
        const isDisabled = document.getElementById('is-disabled') ? document.getElementById('is-disabled').checked : false;
        
        if (!this.validateAge(age)) {
            this.isAnimating = false;
            return;
        }
        
        // 显示加载动画
        this.showLoadingState();
        
        setTimeout(() => {
            const ticketInfo = this.generateTicket(age, isStudent, isDisabled);
            this.displayTicket(ticketInfo);
            this.saveVisitRecord(ticketInfo);
            this.updateStats();
            
            // 显示成功通知
            this.showBubbleNotification(
                '🎫',
                '门票购买成功！',
                `${ticketInfo.finalPrice === 0 ? '免费入园' : '¥' + Math.round(ticketInfo.finalPrice)}`
            );
            
            this.hideLoadingState();
            this.isAnimating = false;
            
            // 平滑滚动到门票显示区域
            const ticketDisplay = document.getElementById('ticket-display');
            if (ticketDisplay) {
                ticketDisplay.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });
            }
        }, 1500);
    }
    
    showLoadingState() {
        const btn = document.querySelector('.purchase-btn');
        if (btn) {
            btn.innerHTML = '<div class="loading"></div> 正在生成门票...';
            btn.disabled = true;
        }
    }
    
    hideLoadingState() {
        const btn = document.querySelector('.purchase-btn');
        if (btn) {
            btn.innerHTML = '<i class="fas fa-ticket-alt"></i> 立即购票';
            btn.disabled = false;
        }
    }
    
    validateAge(age) {
        if (isNaN(age) || age < 0) {
            this.showBubbleNotification('❌', '输入错误', '请输入有效的年龄！');
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
        const weekday = now.getDay();
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
        
        // 夜间模式优惠
        if (this.currentTheme === 'night' && hour >= 19) {
            discount += 0.1;
            specialNotes.push('夜游优惠：9折');
        }
        
        // 节日模式特惠
        if (this.currentTheme === 'festival') {
            discount += 0.15;
            specialNotes.push('节日特惠：85折');
        }
        
        ticketInfo.discount = discount;
        ticketInfo.specialNotes = specialNotes;
        ticketInfo.finalPrice = Math.max(0, ticketInfo.basePrice * (1 - discount));
        
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
        const elements = {
            'ticket-id': ticketId,
            'ticket-age': `${ticketInfo.age}岁`,
            'ticket-type': this.ticketTypeNames[ticketInfo.ticketType],
            'ticket-date': now.toLocaleString('zh-CN')
        };
        
        Object.entries(elements).forEach(([id, value]) => {
            const element = document.getElementById(id);
            if (element) element.textContent = value;
        });
        
        // 价格信息
        this.displayPriceInfo(ticketInfo);
        
        // 特殊说明
        this.displaySpecialNotes(ticketInfo);
        
        // 生成二维码
        this.generateQRCode(ticketId);
        
        // 显示门票并添加动画
        if (ticketDisplay) {
            ticketDisplay.style.display = 'block';
            ticketDisplay.classList.add('show');
        }
        
        // 隐藏表单
        const form = document.querySelector('.ticket-form');
        if (form) {
            form.style.display = 'none';
        }
    }
    
    displayPriceInfo(ticketInfo) {
        const priceElement = document.getElementById('ticket-price');
        const discountInfo = document.getElementById('discount-info');
        
        if (!priceElement) return;
        
        if (ticketInfo.finalPrice === 0) {
            priceElement.innerHTML = '<span class="free-tag">🆓 免费入园</span>';
            if (discountInfo) discountInfo.style.display = 'none';
        } else {
            priceElement.textContent = `¥${Math.round(ticketInfo.finalPrice)}`;
            
            if (ticketInfo.discount > 0 && discountInfo) {
                const originalPrice = document.getElementById('original-price');
                const discountPercent = document.getElementById('discount-percent');
                const finalPrice = document.getElementById('final-price');
                
                if (originalPrice) originalPrice.textContent = `¥${Math.round(ticketInfo.basePrice)}`;
                if (discountPercent) discountPercent.textContent = `${Math.round(ticketInfo.discount * 100)}%`;
                if (finalPrice) finalPrice.textContent = `¥${Math.round(ticketInfo.finalPrice)}`;
                
                discountInfo.style.display = 'block';
            } else if (discountInfo) {
                discountInfo.style.display = 'none';
            }
        }
    }
    
    displaySpecialNotes(ticketInfo) {
        const specialNotes = document.getElementById('special-notes');
        const notesList = document.getElementById('notes-list');
        
        if (!specialNotes || !notesList) return;
        
        if (ticketInfo.specialNotes && ticketInfo.specialNotes.length > 0) {
            notesList.innerHTML = '';
            ticketInfo.specialNotes.forEach(note => {
                const li = document.createElement('li');
                li.textContent = note;
                notesList.appendChild(li);
            });
            specialNotes.style.display = 'block';
        } else {
            specialNotes.style.display = 'none';
        }
    }
    
    generateQRCode(ticketId) {
        const qrElement = document.getElementById('qr-code');
        if (!qrElement) return;
        
        // 创建更精美的二维码艺术
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
        
        qrElement.textContent = qrArt.join('\n');
        
        // 添加动画效果
        qrElement.style.animation = 'qrPulse 3s ease-in-out infinite';
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
        this.dailyStats.currentVisitors = Math.floor(Math.random() * 200) + 50; // 模拟当前游客数
    }
    
    updateStats() {
        const stats = {
            'total-visitors': this.dailyStats.totalVisitors,
            'total-revenue': `¥${Math.round(this.dailyStats.totalRevenue)}`,
            'current-visitors': this.dailyStats.currentVisitors
        };
        
        Object.entries(stats).forEach(([id, value]) => {
            const element = document.getElementById(id);
            if (element) {
                element.textContent = value;
            }
        });
        
        // 计算平均票价
        if (this.dailyStats.totalVisitors > 0) {
            const avgPrice = this.dailyStats.totalRevenue / this.dailyStats.totalVisitors;
            const avgElement = document.getElementById('avg-price');
            if (avgElement) {
                avgElement.textContent = `¥${Math.round(avgPrice)}`;
            }
        }
    }
    
    updateRealTimeStats() {
        // 模拟实时数据更新
        this.dailyStats.currentVisitors += Math.floor(Math.random() * 10) - 5;
        this.dailyStats.currentVisitors = Math.max(0, Math.min(500, this.dailyStats.currentVisitors));
        
        const currentElement = document.getElementById('current-visitors');
        if (currentElement) {
            currentElement.textContent = this.dailyStats.currentVisitors;
        }
    }
    
    resetForm() {
        // 显示表单
        const form = document.querySelector('.ticket-form');
        if (form) {
            form.style.display = 'block';
        }
        
        // 隐藏门票显示
        const ticketDisplay = document.getElementById('ticket-display');
        if (ticketDisplay) {
            ticketDisplay.style.display = 'none';
            ticketDisplay.classList.remove('show');
        }
        
        // 重置表单
        const formElement = document.getElementById('ticket-purchase-form');
        if (formElement) {
            formElement.reset();
        }
        
        // 滚动到表单
        if (form) {
            form.scrollIntoView({
                behavior: 'smooth',
                block: 'center'
            });
        }
        
        // 显示重置通知
        this.showBubbleNotification('🔄', '表单已重置', '准备购买新门票吧！');
    }
}

// 页面增强功能
class PageEnhancer {
    constructor() {
        this.init();
    }
    
    init() {
        this.addInteractiveEffects();
        this.addKeyboardShortcuts();
        this.addScrollEffects();
        this.addLoadingEffects();
    }
    
    addInteractiveEffects() {
        // 按钮波纹效果
        document.addEventListener('click', (e) => {
            if (e.target.matches('button, .btn')) {
                this.createRipple(e);
            }
        });
        
        // 表单焦点效果
        document.querySelectorAll('input, select, textarea').forEach(input => {
            input.addEventListener('focus', () => {
                input.closest('.form-group')?.classList.add('focused');
            });
            
            input.addEventListener('blur', () => {
                input.closest('.form-group')?.classList.remove('focused');
            });
        });
        
        // 卡片悬停效果增强
        document.querySelectorAll('.card, section').forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.transform = 'translateY(-8px) scale(1.02)';
            });
            
            card.addEventListener('mouseleave', () => {
                card.style.transform = '';
            });
        });
    }
    
    createRipple(e) {
        const button = e.target;
        const ripple = document.createElement('span');
        const rect = button.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;
        
        ripple.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            left: ${x}px;
            top: ${y}px;
            background: rgba(255, 255, 255, 0.6);
            border-radius: 50%;
            transform: scale(0);
            animation: ripple-animation 0.6s linear;
            pointer-events: none;
            z-index: 1;
        `;
        
        button.style.position = 'relative';
        button.style.overflow = 'hidden';
        button.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    }
    
    addKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            // Ctrl + Enter 快速购票
            if (e.ctrlKey && e.key === 'Enter') {
                e.preventDefault();
                const purchaseBtn = document.querySelector('.purchase-btn');
                if (purchaseBtn && !purchaseBtn.disabled) {
                    purchaseBtn.click();
                }
            }
            
            // Escape 重置表单
            if (e.key === 'Escape') {
                const newTicketBtn = document.getElementById('new-ticket-btn');
                if (newTicketBtn) {
                    newTicketBtn.click();
                }
            }
        });
    }
    
    addScrollEffects() {
        // 滚动时的视差效果
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const parallax = document.querySelector('.welcome-banner');
            
            if (parallax) {
                const speed = scrolled * 0.5;
                parallax.style.transform = `translateY(${speed}px)`;
            }
        });
        
        // 滚动显示动画
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in');
                }
            });
        }, observerOptions);
        
        document.querySelectorAll('.price-item, .discount-list li, .info-card').forEach(el => {
            observer.observe(el);
        });
    }
    
    addLoadingEffects() {
        // 页面加载完成后的入场动画
        window.addEventListener('load', () => {
            document.body.classList.add('loaded');
            
            // 依次显示各个部分
            const sections = document.querySelectorAll('section');
            sections.forEach((section, index) => {
                setTimeout(() => {
                    section.style.animation = `slideInUp 0.6s ease-out ${index * 0.1}s both`;
                }, 100);
            });
        });
    }
}

// 初始化系统
document.addEventListener('DOMContentLoaded', () => {
    // 初始化门票系统
    const ticketSystem = new TicketSystem();
    
    // 初始化页面增强功能
    const pageEnhancer = new PageEnhancer();
    
    // 添加全局样式
    const globalStyles = document.createElement('style');
    globalStyles.textContent = `
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
        
        .loaded {
            animation: none;
        }
        
        .free-tag {
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: bold;
            box-shadow: 0 4px 15px rgba(17, 153, 142, 0.3);
        }
        
        .theme-btn.active {
            transform: scale(1.2);
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
        }
    `;
    
    document.head.appendChild(globalStyles);
    
    // 显示欢迎消息
    setTimeout(() => {
        ticketSystem.showBubbleNotification(
            '🎉',
            '欢迎来到47游乐园！',
            '体验最炫酷的购票系统'
        );
    }, 1000);
});
