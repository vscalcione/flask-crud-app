create table billing_address(
    id int(3) not null primary key auto_increment,
    address_line_1 varchar(200) not null,
    address_line_2 varchar(200) not null,
    city varchar(50) not null,
    state varchar(50) not null,
    zip_code varchar(25) not null
);
create table shipping_address(
    id int(3) not null primary key auto_increment,
    address_line_1 varchar(200) not null,
    address_line_2 varchar(200) not null,
    city varchar(50) not null,
    state varchar(50) not null,
    zip_code varchar(25) not null
);

create table customer(
    id int(3) primary key auto_increment not null,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    email varchar(255) not null,
    phone_number varchar(50) not null,
    id_billing_address int(3),
    id_shipping_address int(3),
    foreign key(id_billing_address) references billing_address (id),
    foreign key(id_shipping_address) references shipping_address (id)
);

create table user(
    id int(3) not null primary key auto_increment,
    username varchar(50) not null,
    password varchar(50) not null,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    email varchar(255) not null,
    phone_number varchar(50) not null,
    id_billing_address int(3) not null,
    id_shipping_address int(3) not null,
    foreign key(id_billing_address) references billing_address (id),
    foreign key(id_shipping_address) references shipping_address (id)
);

create table product(
    id int(3) not null primary key auto_increment,
    description varchar(500) not null,
    price varchar(50) not null,
    image_url varchar(200) not null
);