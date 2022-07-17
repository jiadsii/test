//微信读书5.5.1以后的版本加入了验证不能使用
var body = $response.body;
var obj = JSON.parse(body);
obj.isPaying= 1;
obj.day= 91;
obj.remainTime= 99306196;
obj.payingRemainTime= 3213131221;
obj.savedMoney= 9927433;
obj.totalFreeReadDay= 6666;
obj.remainCoupon= 6666;
obj.remainCount= 6666;
body = JSON.stringify(obj);
$done({body});
