PREFIX ?= /usr/local

CC = gcc
AR = ar
#AR = dllwrap

CFLAGS = -std=gnu99 -fPIC -Wall -Wno-unused-parameter -Wno-unused-function
CFLAGS += -I. -O3 -fno-strict-overflow -lwinpthread -I./contrib -I./common
LDFLAGS = -lwinpthread

#APRILTAG_SRCS := $(shell ls *.c common/*.c)
APRILTAG_SRCS := apriltag.c \
								 apriltag_family.c \
								 apriltag_quad_thresh.c \
								 g2d.c \
								 tag16h5.c \
								 tag25h7.c \
								 tag25h9.c \
								 tag36artoolkit.c \
								 tag36h10.c \
								 tag36h11.c \
								 common/getopt.c \
								 common/homography.c \
								 common/image_f32.c \
								 common/image_u8.c \
								 common/image_u32.c \
								 common/matd.c \
								 common/pnm.c \
								 common/string_util.c \
								 common/svd22.c \
								 common/time_util.c \
								 common/unionfind.c \
								 common/workerpool.c \
								 common/zarray.c \
								 common/zhash.c \
								 common/zmaxheap.c \
								 contrib/apriltag_quad_contour.c \
								 contrib/apriltag_vis.c \
								 contrib/box.c \
								 contrib/contour.c \
								 contrib/lm.c \
								 contrib/pdfutil.c \
								 contrib/pose.c

APRILTAG_HEADERS := apriltag.h \
								  apriltag_family.h \
									g2d.h \
									tag16h5.h \
									tag25h7.h \
									tag25h9.h \
									tag36artoolkit.h \
									tag36h10.h \
									tag36h11.h \
									common/assert_with_unused.h \
									common/getopt.h \
									common/homography.h \
									common/image_f32.h \
									common/image_u8.h \
									common/image_u32.h \
									common/matd.h \
									common/math_util.h \
									common/postscript_utils.h \
									common/string_util.h \
									common/svd22.h \
									common/thash_impl.h \
									common/time_util.h \
									common/timeprofile.h \
									common/unionfind.h \
									common/workerpool.h \
									common/zarray.h \
									common/zhash.h \
									common/zmaxheap.h \
									contrib/apriltag_quad_contour.h \
									contrib/apriltag_vis.h \
									contrib/box.h \
									contrib/contour.h \
									contrib/lm.h \
									contrib/pdfutil.h \
									contrib/pose.h

APRILTAG_OBJS := $(APRILTAG_SRCS:%.c=%.o)
TARGETS := apriltag_demo libapriltag.a libapriltag.dll

.PHONY: all
all: $(TARGETS)
	@$(MAKE) -C example all

.PHONY: install
install: libapriltag.so
	@chmod +x install.sh
	@./install.sh $(PREFIX)/lib libapriltag.so
	@./install.sh $(PREFIX)/include/apriltag $(APRILTAG_HEADERS)
	@ldconfig

apriltag_demo: apriltag_demo.o $(APRILTAG_OBJS)
		@echo "   [$@]"
		@$(CC) -o $@ $^ $(LDFLAGS)

libapriltag.a: $(APRILTAG_OBJS)
	@echo "   [$@]"
	@$(AR) -cq $@ $(APRILTAG_OBJS)

libapriltag.dll: $(APRILTAG_OBJS)
	@echo "   [$@]"
	@$(CC) -fPIC -shared -o $@ $^



%.o: %.c
	@echo "   $@"
	@$(CC) -o $@ -c $< $(CFLAGS)

.PHONY: clean
clean:
	@del /s "*.o"
	@del /s "apriltag_demo.exe"
	@del $(TARGETS)
#	@del $(APRILTAG_OBJS) apriltag_demo.o $(TARGETS)
#	@$(MAKE) -C example clean
